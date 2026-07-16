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
load_dotenv()
MODEL = "llama-3.1-8b-instant"
def multiply(a:int,b:int)->int:
    """Multipy two int and return the excat result """
    return a*b
@tool
def word_count(text:str) -> int:
    """Count how many words are there in text"""
    return len (text.split())
TOOLS = [multiply, word_count]
questions = [
    "What is 24 * 7?",              
    "How many words in 'the quick brown fox jumps'?",  
    "Say hello in one word.",
]
from langchain_groq import ChatGroq
llm = ChatGroq(model=MODEL,temperature=0)
llm_with_tools = llm.bind_tools(TOOLS)
for q in questions:
    print("=" * 60)
    print(f"Q: {q}")
    resp = llm_with_tools.invoke(q)

    if resp.tool_calls:
        # The model asked for a tool -- it did NOT answer yet.
        for call in resp.tool_calls:
            print(f"  model wants tool: {call['name']}  args={call['args']}")
        print("  (content is empty -- the model is waiting for the tool result)")
    else:
        # No tool needed -- the model just answered.
        print(f"  no tool needed. answer: {resp.content}")