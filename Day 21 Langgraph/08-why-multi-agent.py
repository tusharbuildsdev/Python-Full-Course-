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