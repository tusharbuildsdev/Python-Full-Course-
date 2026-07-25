"""
04 - Reducers: make state ADD UP instead of overwrite.

By default, when a node returns {"key": value}, that value REPLACES the old
one. Fine for a str or int. But for a LIST you're building up (a chat history,
a log of steps), replacing throws away everything so far.

A REDUCER changes how updates merge. You attach it to a field with Annotated:

    from operator import add
    log: Annotated[list, add]          # updates get concatenated, not replaced

For chat messages, LangGraph ships a smarter reducer, add_messages, that also
turns ("human", "hi") tuples into proper Message objects and handles updates by
id. State whose messages field uses it is so common there's a prebuilt
MessagesState you can subclass.

This whole file is offline -- it's about how state merges, no model call.

Setup:
    pip install langgraph langchain-core
Run:
    python reducers_and_messages.py
"""

from typing import TypedDict, Annotated
from operator import add
from langgraph.graph import StateGraph, START, END, MessagesState
from langgraph.graph.message import add_messages


class NoReducer(TypedDict):
    log: list


def step_a(state):
    return {"log": ["a ran"]}


def step_b(state):
    return {"log": ["b ran"]}  # replaces a's list entirely!


b1 = StateGraph(NoReducer)
b1.add_node("step_a", step_a)
b1.add_node("step_b", step_b)
b1.add_edge(START, "step_a")
b1.add_edge("step_a", "step_b")
b1.add_edge("step_b", END)
print("PART A (no reducer): log =", b1.compile().invoke({"log": []})["log"])
print("  -> b's update REPLACED a's. History lost.\n")
