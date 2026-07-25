from pathlib import Path

SAMPLE = Path(__file__).resolve().parent / "hello.txt"
print(SAMPLE)


def read_whole_file() -> str:
    with open(SAMPLE, "r", encoding="utf-8") as f:
        return f.read()


print(read_whole_file())


def read_as_line() -> list:
    with open(SAMPLE, "r", encoding="utf-8") as f:
        return f.read()


print(read_as_line())


def read_line_by_line() -> None:
    """Loop the file one line at a time - the memory-friendly way for big files."""
    # Iterating the file object streams it: only one line is in memory at a time.
    with open(SAMPLE, "r", encoding="utf-8") as f:
        for number, line in enumerate(f, start=1):
            print(f"  line {number}: {line.rstrip()}")


def write_sample() -> None:
    with open(SAMPLE, "w", encoding="utf-8") as f:
        f.write("Line 1: Chroma stores vectors.\n")
        f.write("Line 2: Embeddings turn text into meaning.\n")


write_sample()
print()
