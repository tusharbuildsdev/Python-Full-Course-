# 45 Days of LLM Engineering

> A hands-on 45-day roadmap to build real-world LLM applications with Python.

Learn the essential skills behind modern AI products: Python, prompt engineering, embeddings, retrieval-augmented generation (RAG), LangChain, LangGraph, and agent workflows. Every lesson is designed to be short, focused, and runnable.

## What you will build

- Python foundations for AI development
- LLM prompts and conversational chatbots
- Embedding search and RAG pipelines
- Streamlit interfaces and document-chat apps
- LangChain workflows, tools, and structured output
- LangGraph state machines and multi-agent patterns

## Course roadmap

| Phase | Days | Focus |
| --- | ---: | --- |
| [Phase 1 - Foundations](45-Days-LLM-Engineering/Phase-1-Foundations/README.md) | 01-15 | Python, APIs, prompting, chatbots, and embeddings |
| [Phase 2 - RAG and Memory](45-Days-LLM-Engineering/Phase-2-RAG-and-Memory/README.md) | 16-20 | Vector search, document chat, Streamlit, and LangChain |
| [Phase 3 - Agents and Tools](45-Days-LLM-Engineering/Phase-3-Agents-and-Tools/README.md) | 21-45 | LangGraph, tools, multi-agent systems, evaluation, and deployment |

## Repository structure

```text
45-Days-LLM-Engineering/
|-- Phase-1-Foundations/        # Days 01-15
|-- Phase-2-RAG-and-Memory/     # Days 16-20
`-- Phase-3-Agents-and-Tools/   # Days 21-45
```

Each day follows a predictable, self-contained format:

```text
Day-XX-Topic/
|-- README.md                   # Learning goals and setup notes
|-- 01-concept-name/            # Focused module with runnable code
|-- 02-next-concept/
`-- exercises/                  # Practice work, where applicable
```

## Quick start

```powershell
git clone https://github.com/tusharbuildsdev/Python-Full-Course-.git
cd "Python Complete Course"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

The root [requirements.txt](requirements.txt) contains dependencies used across the course. For API-based lessons, create a local `.env` file and add your own credentials; never commit it.

## Run a lesson

Run an example from its own module directory so relative paths work correctly:

```powershell
cd 45-Days-LLM-Engineering\Phase-1-Foundations\Day-12-Prompt-Engineering\05-first-calls
python first_calls.py
```

For Streamlit projects:

```powershell
streamlit run app.py
```

## Current progress

Days 01-21 are available now. The remaining Phase 3 folders are reserved for the upcoming agent, evaluation, deployment, and capstone modules.

## Connect

- GitHub: [@tusharbuildsdev](https://github.com/tusharbuildsdev)
- LinkedIn: [Tushar Verma](https://www.linkedin.com/in/tusharbuildsdev)

If this course helps you, consider starring the repository and sharing it with another learner.
