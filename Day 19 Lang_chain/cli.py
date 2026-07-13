from dotenv import load_dotenv
import os

from langchain_groq import ChatGroq

from langchain_core.prompts import ChatPromptTemplate
load_dotenv()
MODEL_NAME = "llama-3.1-8b-instant"
TEMPERATURE = 0

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are a helpful AI assistant.

        Rules:
        - Never repeat the same sentence.
        - If you don't know something, say "I don't know."
        - Keep answers concise.
        - Do not make up information.
        """
    ),
    ("human", "{question}")
])
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

chain = prompt | llm

# Check API Key
if not os.getenv("GROQ_API_KEY"):
    raise ValueError("GROQ_API_KEY not found in .env file")

# Create LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

print("=" * 50)
print("🤖 Welcome to CLI Chatbot")
print("Type 'exit' to quit")
print("=" * 50)

while True:
    user_input = input("\nYou: ").strip()

    if user_input.lower() == "exit":
        print("\n👋 Goodbye!")
        break

    if not user_input:
        print("⚠️ Please enter a message.")
        continue

    try:
        response = llm.invoke(user_input)
        print(f"\nBot: {response.content}")

    except Exception as e:
        print(f"\n❌ Error: {e}")

    response = chain.invoke({
    "question": user_input
})

print(response.content)