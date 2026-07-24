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