import chromadb
from config import COLLECTION_NAME


class VectorStore:
    def __init__(self, embedder):
        self._embedder = embedder
        self._client = chromadb.EphemeralClient()
        self._next_id = 0
        self._make_collection()

    def _make_collection(self):
        self._collection = self._client.get_or_create_collection(
            name=COLLECTION_NAME,
            metadata={"hnsw:space": "cosine"},
        )

    def add_texts(self, chunks: list, source: str) -> int:
        """Embed `chunks` and store them, tagged with their `source` filename."""
        if not chunks:
            return 0

        embeddings = self._embedder.encode(chunks).tolist()

        ids = []
        for _ in chunks:
            ids.append(f"chunk={self._next_id}")
            self._next_id += 1

        self._collection.add(
            ids=ids,
            documents=chunks,
            embeddings=embeddings,
            metadatas=[{"source": source} for _ in chunks],
        )

        return len(chunks)

    def search(self, query: str, k: int) -> list:
        if self.count() == 0:
            return []

        query_vec = self._embedder.encode(query).tolist()

        result = self._collection.query(
            query_embeddings=[query_vec],
            n_results=k,
            include=["documents", "metadatas", "distances"],
        )

        matches = []

        for document, metadata, distance in zip(
            result["documents"][0],
            result["metadatas"][0],
            result["distances"][0],
        ):
            matches.append(
                {
                    "document": document,
                    "source": metadata.get("source", "unknown"),
                    "similarity": 1 - distance,
                }
            )

        return matches

    def count(self) -> int:
        return self._collection.count()

    def reset(self) -> None:
        """Delete everything - powers the sidebar's 'Clear documents' button."""
        self._client.delete_collection(COLLECTION_NAME)
        self._next_id = 0
        self._make_collection()


if __name__ == "__main__":
    from sentence_transformers import SentenceTransformer
    from config import EMBED_MODEL_NAME

    store = VectorStore(SentenceTransformer(EMBED_MODEL_NAME))

    store.add_texts(
        [
            "Refunds are processed within 5 business days.",
            "Our office is open Monday to Friday.",
            "You can reset your password from the settings page.",
        ],
        source="faq.txt",
    )

    print("Stored chunks:", store.count())

    for m in store.search(
        "how long does getting money back take?",
        k=2,
    ):
        print(f"{m['similarity']:.3f}  [{m['source']}]  {m['document']}")
