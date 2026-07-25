from config import SYSTEM_PROMPT


def build_context_block(matches: list) -> str:
    if not matches:
        return "No document retrieved"

    lines = []

    for i, match in enumerate(matches, start=1):
        lines.append(
            f"[Source {i} | file:{match['source']}] | "
            f"relevance:{match['similarity']:.2f}\n"
            f"{match['document']}"
        )

    return "\n\n".join(lines)


def build_messages(question: str, matches: list, history: list) -> list:

    context_block = build_context_block(matches)

    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    messages.extend(history)

    messages.append(
        {
            "role": "user",
            "content": (
                f"Context from the user's documents:\n{context_block}\n\n"
                f"Question: {question}"
            ),
        }
    )

    return messages


if __name__ == "__main__":
    fake_matches = [
        {
            "document": "Refunds take 5 business days.",
            "source": "faq.txt",
            "similarity": 0.81,
        },
        {
            "document": "Support is open Mon-Fri.",
            "source": "faq.txt",
            "similarity": 0.44,
        },
    ]

    msgs = build_messages("How long for a refund?", fake_matches, history=[])

    for m in msgs:
        print(f"--- {m['role']} ---")
        print(m["content"])
        print()
