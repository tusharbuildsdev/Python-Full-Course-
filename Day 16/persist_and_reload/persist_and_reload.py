from pathlib import Path
import chromadb

BASE_DIR = Path(__file__).resolve().parent
DB_DIR = BASE_DIR / "chroma_store"
COLLECTION_NAME = "student_notes"


def main() -> None:
    print(f"Database Path: {DB_DIR}")

    client = chromadb.PersistentClient(path=str(DB_DIR))

    print("Available Collections:")
    for collection in client.list_collections():
        print(f"- {collection.name}")

    try:
        collection = client.get_collection(COLLECTION_NAME)
    except Exception:
        print(f"\nCollection '{COLLECTION_NAME}' not found!")
        return

    snapshot = collection.get(include=["documents", "metadatas"])

    print(f"\nTotal Records: {collection.count()}\n")

    for doc_id, metadata, document in zip(
        snapshot["ids"],
        snapshot["metadatas"],
        snapshot["documents"],
    ):
        topic = metadata.get("topic", "unknown")
        print(f"{doc_id} [{topic}]")
        print(document)
        print("-" * 50)


if __name__ == "__main__":
    main()
