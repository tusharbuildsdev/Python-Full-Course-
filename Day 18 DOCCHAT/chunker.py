from config import CHUNK_OVERLAP_WORDS, CHUNK_SIZE_WORDS

def chunk_text(
    text: str,
    size: int = CHUNK_SIZE_WORDS,
    overlap: int = CHUNK_OVERLAP_WORDS
) -> list:

    words = text.split()

    if not words:
        return []

    step = max(1, size - overlap)

    chunks = []

    for start in range(0, len(words), step):
        # Take a window of `size` words starting at `start`.
        window = words[start:start + size]
        chunks.append(" ".join(window))

        # If this window already reached the end, stop.
        if start + size >= len(words):
            break

    return chunks


# Self-test: chunk a numbered string so the overlap is easy to see.
if __name__ == "__main__":
    sample = " ".join(f"w{i}" for i in range(1, 26))   # w1 w2 ... w25
    pieces = chunk_text(sample, size=10, overlap=3)

    print(f"{len(pieces)} chunks from 25 words (size=10, overlap=3):")

    for i, piece in enumerate(pieces, 1):
        print(f"  chunk {i}: {piece}")