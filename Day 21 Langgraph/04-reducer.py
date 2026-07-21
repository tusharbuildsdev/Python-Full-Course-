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