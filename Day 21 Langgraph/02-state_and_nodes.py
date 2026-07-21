"""
02 - State & Nodes: how data flows through a multi-step graph.

The one idea to take from this file:
    A NODE IS A FUNCTION. It receives the whole state and returns ONLY the
    keys it changed. LangGraph merges that partial update back into the state
    before the next node runs.

We build a 3-node text pipeline that shares one state:
    clean  ->  count_words  ->  summarize_shape
Each node adds/updates a different key. By the end, the state holds the work
of all three. No API key needed -- this is all plain Python inside the graph.

Setup:
    pip install langgraph
Run:
    python state_and_nodes.py
"""

from typing import TypedDict
from langgraph.graph import StateGraph, START, END
class State(TypedDict):
    raw: str          # the original input
    cleaned: str      # filled by clean()
    word_count: int   # filled by count_words()
    shape: str        # filled by summarize_shape()

def clean(state: State) -> dict:
    text = state["raw"].strip().replace("  ", " ")
    print(f"[clean]  '{state['raw']}' -> '{text}'")
    return {"cleaned": text}