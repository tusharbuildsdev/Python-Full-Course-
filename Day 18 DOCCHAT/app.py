import streamlit as st
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
import config
from file_loader import load_text
from chunker import chunk_text
from vector_store import VectorStore
from rag import build_messages
from llm import make_client,stream_answer
load_dotenv()
st.set_page_config(page_title="Chat with Docs", page_icon="")
@st.cache_resource
def get_embedder():
    return SentenceTransformer(config.EMBED_MODEL_NAME)
@st.cache_resource
def get_client():
    return make_client()

embedder = get_embedder()
client = get_client()

if "store" not in st.session_state:
    st.session_state.store = VectorStore(embedder)
if "messages" not in st.session_state:
    st.session_state.messages=[]
if "indexed" not in st.session_state:
    st.session_state.indexed=[]
    
store = st.session_state.store
    
st.sidebar.header("⚙️ Model settings")
model = st.sidebar.selectbox("Model", config.GROQ_MODELS)
temperature = st.sidebar.slider(
    "Temperature", 0.0, 1.0, config.DEFAULT_TEMPERATURE, 0.05,
    help="Low = focused and factual. High = more creative.",
)
max_tokens = st.sidebar.slider(
    "Max answer length (tokens)", 128, 2048, config.DEFAULT_MAX_TOKENS, 64,
)
top_k = st.sidebar.slider(
    "Chunks to retrieve (k)", 1, 8, config.TOP_K,
    help="How many document snippets to feed the model per question.",
)

st.sidebar.divider()
if st.sidebar.button("🗑️ Clear documents & chat", width="stretch"):
    store.reset()
    st.session_state.indexed = []
    st.session_state.messages = []
    st.rerun()   

st.sidebar.caption(f"Indexed chunks: {store.count()}")
st.title("📄 Chat With Your Documents")
st.write("Upload PDF, DOCX or TXT files, then ask questions grounded in them.")

if client is None:
    st.error(
        "No GROQ_API_KEY found. Create a .env file with "
        "`GROQ_API_KEY=your_key_here`, then restart the app."
    )
    st.stop()

uploads = st.file_uploader(
    "Upload documents",
    type=["pdf", "docx", "txt"],
    accept_multiple_files=True,
)

for uploaded in uploads or []:
    if uploaded.name in st.session_state.indexed:
        continue
    try:
        text = load_text(uploaded.name, uploaded.getvalue())
        chunks = chunk_text(text)
        added = store.add_texts(chunks, source=uploaded.name)
        st.session_state.indexed.append(uploaded.name)
        st.success(f"Indexed {added} chunks from {uploaded.name}")
    except ValueError as err:
        st.warning(str(err))

if store.count() == 0:
    st.info("Upload at least one document to start chatting.")
    st.stop()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

question = st.chat_input("Ask something about your documents")

if question:
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.write(question)

    matches = store.search(question, k=top_k)

    history = st.session_state.messages[:-1]
    messages = build_messages(question, matches, history)

    with st.chat_message("assistant"):
        reply = st.write_stream(
            stream_answer(client, model, messages, temperature, max_tokens)
        )
        with st.expander("📚 Sources used"):
            for i, m in enumerate(matches, 1):
                st.markdown(
                    f"**Source {i}** · `{m['source']}` · "
                    f"relevance {m['similarity']:.2f}"
                )
                st.caption(m["document"])

    st.session_state.messages.append({"role": "assistant", "content":reply})