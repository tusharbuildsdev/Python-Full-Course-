import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

st.set_page_config(page_title="Groq Chat", page_icon="💬")

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title(" Chat with Groq")

model = st.sidebar.selectbox(
    "Model", ["llama-3.1-8b-instant", "llama-3.3-70b-versatile"]
)

if "messages" not in st.session_state:
    st.session_state.messages = []

if st.sidebar.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# Display messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
prompt = st.chat_input("Ask me anything...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    response = client.chat.completions.create(
        model=model, messages=st.session_state.messages
    )

    answer = response.choices[0].message.content

    st.session_state.messages.append({"role": "assistant", "content": answer})

    with st.chat_message("assistant"):
        st.markdown(answer)
