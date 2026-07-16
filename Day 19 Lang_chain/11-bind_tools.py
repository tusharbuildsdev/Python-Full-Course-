"""
03 - Binding tools to a model: llm.bind_tools([...]).

Once bound, the model can answer with a TOOL CALL instead of prose. It reads the
schemas from module 02 and decides, on its own, which tool (if any) fits the
question. We just read resp.tool_calls.

With GROQ_API_KEY set, this calls a real model and shows its choices. Without a
key, it prints the exact tool schemas the model WOULD receive -- so you still see
what .bind_tools() does.

Setup:
    pip install langchain langchain-groq python-dotenv
Run:
    python bind_tools.py
"""

import os
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_core.utils.function_calling import convert_to_openai_tool
