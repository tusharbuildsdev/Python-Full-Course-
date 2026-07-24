"""
Day 26 - Module 02: Sequential agents (the assembly line)

The simplest team shape: agents in a straight line, each doing ONE job and handing
its work to the next through the shared state.

    START -> [researcher] -> [writer] -> [editor] -> END

Every node is a real LLM call with a different SYSTEM PROMPT -- that system prompt
is what turns one model into a "researcher" vs a "writer" vs an "editor". This is
role-based multi-agent in its purest form.

Run it (needs a free GROQ_API_KEY in a .env file next to this script):
    python sequential_agents.py
"""

from typing import TypedDict

from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START, END
llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)


# --- Shared state: the "desk" the work moves across --------------------------
class State(TypedDict):
    topic: str      # the input (set by us)
    research: str   # filled by the researcher
    draft: str      # filled by the writer
    final: str      # filled by the editor
def _ask(role_system: str, user: str) -> str:
    """Run one LLM call as a given role. This is the whole 'agent' -- a role + a call."""
    reply = llm.invoke([SystemMessage(content=role_system), HumanMessage(content=user)])
    return reply.content.strip()
def researcher(state: State) -> dict:
    