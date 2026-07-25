from pathlib import Path
import chromadb
from sentence_transformers import SentenceTransformer

BASE_DIR = Path(__file__).resolve().parent
print(BASE_DIR)
DB_DIR = BASE_DIR / "chroma_store"
COLLECTION_NAME = "student_notes"
NOTES = [
    {
        "id": "1",
        "topic": "Python",
        "document": "Python is an easy programming language.",
    },
    {
        "id": "2",
        "topic": "AI",
        "document": "Artificial Intelligence enables machines to learn.",
    },
]


def main() -> None:
    model = SentenceTransformer("all-MiniLM-L6-v2")
    documents = [note["document"] for note in NOTES]
    embeddings = model.encode(documents).tolist()
    client = chromadb.PersistentClient(path=str(DB_DIR))
    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"},
    )
    collection.upsert(
        ids=[note["id"] for note in NOTES],
        documents=documents,
        metadatas=[{"topic": note["topic"]} for note in NOTES],
        embeddings=embeddings,
    )
    print(f" stored records : {collection.count()}")


if __name__ == "__main__":
    main()
