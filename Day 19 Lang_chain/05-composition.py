"""
05 - Runnables: branching and combining steps (beyond a straight line).

A chain isn't always a straight pipe. Sometimes you need to:
  * run several steps on the SAME input and collect the results  -> RunnableParallel
  * pass the input through UNCHANGED alongside a computed value   -> RunnablePassthrough
  * drop any plain function into the flow                         -> RunnableLambda

These three are the glue for real pipelines (including RAG). Best part: this
whole file runs OFFLINE - no key needed - because composition is pure Python.

Setup:
    pip install langchain
Run:
    python composition.py
"""
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import (
    RunnableLambda,
    RunnableParallel,
    RunnablePassthrough,
)
