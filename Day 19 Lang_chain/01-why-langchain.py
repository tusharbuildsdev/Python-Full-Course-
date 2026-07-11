# pip install langchain
# pip install langchain-groq
# pip install python-dotenv

from dotenv import load_dotenv
import os

from langchain_core.messages import SystemMessage, HumanMessage
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()

# Messages
messages = [
    SystemMessage(content="You are a helpful Assistant"),
    HumanMessage(content="Explain What is API?")
]

# Print messages
for m in messages:
    print(f"[{m.type}] {m.content}")

# Check API Key
if not os.getenv("GROQ_API_KEY"):
    print("NO API KEY")
else:
    model = ChatGroq(model="llama-3.1-8b-instant")
    reply = model.invoke(messages)
    print("Reply type:", type(reply).__name__)   # AIMessage
    print("Answer    :", reply.content)