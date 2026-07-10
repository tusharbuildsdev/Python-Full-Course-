GROQ_MODELS =[
    "llama-3.1-8b-instant",       # fast + cheap, great default
    "llama-3.3-70b-versatile",    # smarter, a little slower
    "openai/gpt-oss-20b",

]

DEFAULT_TEMPERATURE=0.2
DEFAULT_MAX_TOKENS=512
EMBED_MODEL_NAME = "all-MiniLM-L6-v2"
CHUNK_SIZE_WORDS = 120
CHUNK_OVERLAP_WORDS = 20
TOP_K=4
COLLECTION_NAME="UPLOADED_DOCS"
SYSTEM_PROMPT=(
    
    "You are a helpful assistant that answers questions based on the context provided. "
    "If the answer is not contained within the context, respond with 'I don't know.' "
    "Do not fabricate information or provide answers that are not supported by the context."
)