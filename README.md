# 45 Days of LLM Engineering

A practical, build-first curriculum for progressing from Python fundamentals to retrieval-augmented generation (RAG), memory, agents, and production-ready AI tools.

## Learning path

| Phase | Days | Focus |
| --- | ---: | --- |
| [Phase 1 — Foundations](45-Days-LLM-Engineering/Phase-1-Foundations/README.md) | 1–15 | Python, APIs, prompting, chatbots, and embeddings |
| [Phase 2 — RAG & Memory](45-Days-LLM-Engineering/Phase-2-RAG-and-Memory/README.md) | 16–20 | Vector search, document chat, Streamlit, and LangChain |
| [Phase 3 — Agents & Tools](45-Days-LLM-Engineering/Phase-3-Agents-and-Tools/README.md) | 21–45 | LangGraph, tools, multi-agent patterns, and deployment |

## Repository layout

```text
45-Days-LLM-Engineering/
├── Phase-1-Foundations/        # Days 01–15
├── Phase-2-RAG-and-Memory/     # Days 16–20
└── Phase-3-Agents-and-Tools/   # Days 21–45
```

Each day is self-contained:

```text
Day-XX-Topic/
├── README.md              # Learning goals and setup
├── 01-concept/            # A focused concept with runnable code
├── 02-next-concept/
└── exercises/             # Practice work, when applicable
```

## Getting started

```powershell
git clone <your-repository-url>
cd "Python Complete Course"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the `requirements.txt` from the lesson you are running when it is present. If an example uses an API key, create a local `.env` file and never commit it.

## Run an example

Run every example from its own folder so relative paths work as intended:

```powershell
cd 45-Days-LLM-Engineering\Phase-1-Foundations\Day-12-Prompt-Engineering\05-first-calls
python first_calls.py
```

For Streamlit lessons:

```powershell
streamlit run app.py
```

## Progress

Days 01–21 are currently included. The remaining Phase 3 days are intentionally reserved in the roadmap so the course can grow without changing its public structure.
