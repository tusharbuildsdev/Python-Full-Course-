"""
Day 26 - Module 01: Why multi-agent? (and the three shapes)

The big idea: an "agent" is just a NODE in a LangGraph graph. Once you see that,
building a *team* of agents is nothing new -- it's the same StateGraph you learned
on Day 24, with more than one worker wired in.

This script needs NO API key and NO LLM. It builds a tiny two-"agent" graph out of
plain Python functions so you can see the shape, then prints the three team shapes
you'll build across today's modules.

Run it:
    python why_multi_agent.py
"""

from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    topic: str
    draft: str
    log: list


def writer(state: State) -> dict:
    """Agent #1: turns a topic into a rough one-liner."""
    draft = f"{state['topic']} is useful because it saves people time."
    return {"draft": draft, "log": ["writer wrote a rough draft"]}


def editor(state: State) -> dict:
    """Agent #2: polishes whatever the writer handed over via the state."""
    polished = state["draft"].replace("useful", "genuinely useful").rstrip(".") + "!"
    # Carry the log forward by hand (a plain list key OVERWRITES otherwise -- you'll
    # meet `reducers`, the proper fix for accumulating lists, in Module 04).
    return {"draft": polished, "log": state["log"] + ["editor polished the draft"]}


def build_team():
    """Wire the two agents into a straight line: writer -> editor."""
    g = StateGraph(State)
    g.add_node("writer", writer)
    g.add_node("editor", editor)
    g.add_edge(START, "writer")  # start hands the topic to the writer
    g.add_edge("writer", "editor")  # writer hands the draft to the editor
    g.add_edge("editor", END)
    return g.compile()
