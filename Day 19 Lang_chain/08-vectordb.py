"""
02 - Vector store & retriever: make chunks searchable with LangChain.

Day 18 did this by hand: embed every doc, store the vectors, cosine-compare a
query. LangChain wraps all of that in a VECTOR STORE. You hand it Documents +
an embeddings model; it embeds and indexes them. Then .as_retriever() gives you
a RETRIEVER -- a standard Runnable whose .invoke(query) returns the top matching
Documents.

Embeddings run LOCALLY (sentence-transformers via HuggingFaceEmbeddings) -- no
API key, nothing leaves your machine. Chroma here is IN-MEMORY (nothing saved to
disk), which is perfect for a demo or a per-session app.

Setup:
    pip install langchain-chroma langchain-huggingface sentence-transformers
Run:
    python vectorstore.py
"""

import warnings
warnings.filterwarnings("ignore")            # hide noisy model-loading warnings

from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
docs = [
    Document(page_content="Refunds are processed within 5 business days to the original payment method.",
             metadata={"source": "refunds"}),
    Document(page_content="We ship across India; standard delivery takes 4 to 7 working days.",
             metadata={"source": "shipping"}),
    Document(page_content="Reach support at help@example.in or 1800-123-456, 9am to 6pm.",
             metadata={"source": "support"}),
    Document(page_content="Cash on delivery is available for orders under 5000 rupees.",
             metadata={"source": "payment"}),
]
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
store = Chroma.from_documents(docs, embedding=embeddings)
print(f"Indexed {len(docs)} documents in an in-memory Chroma store.\n")
query = "how do I get my money back?"
hits = store.similarity_search(query, k=2)
print(f"similarity_search({query!r}, k=2):")
for d in hits:
    print(f"  [{d.metadata['source']:8}] {d.page_content}")
print()

# Want the scores too? similarity_search_with_score returns (Document, distance).
print("with scores (lower distance = closer):")
for d, score in store.similarity_search_with_score(query, k=2):
    print(f"  {score:.3f}  [{d.metadata['source']}]")
print()

# --- 4b. The retriever: the store as a Runnable ---------------------------
# This is the piece that matters for RAG. .as_retriever() wraps the store as a
# standard Runnable: retriever.invoke(query) -> list[Document]. Because it's a
# Runnable, it drops straight into a | chain (module 03).
retriever = store.as_retriever(search_kwargs={"k": 2})
results = retriever.invoke("when will my order arrive?")
print("retriever.invoke('when will my order arrive?'):")
for d in results:
    print(f"  [{d.metadata['source']:8}] {d.page_content}")
print()

print("Takeaway: Documents + local embeddings -> Chroma -> .as_retriever().")
print("A retriever is just a Runnable that returns Documents -- RAG's 'R'.")
print("Next: pipe it into a prompt|model|parser chain to get grounded answers.")