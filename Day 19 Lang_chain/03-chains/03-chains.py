from dotenv import load_dotenv
import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()

MODEL = "llama-3.1-8b-instant"

# -----------------------------
# Runnable Example
# -----------------------------
to_upper = RunnableLambda(lambda s: s.upper())
add_bang = RunnableLambda(lambda s: s + "!")
tiny_chain = to_upper | add_bang

print(tiny_chain.invoke("hello"))

# -----------------------------
# Prompt Template
# -----------------------------
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Answer in one short sentence."),
        ("human", "{question}"),
    ]
)

# Output Parser
parser = StrOutputParser()

# -----------------------------
# Check API Key
# -----------------------------
if not os.getenv("GROQ_API_KEY"):
    print("No API Key Found!")
else:
    # Create Model
    model = ChatGroq(model=MODEL, temperature=0)

    # LCEL Chain
    chain = prompt | model | parser

    # Invoke Chain
    answer = chain.invoke({"question": "What is Python?"})
    print(answer)

    answer2 = chain.stream({"question": "what are 3 newton's law of moation"})
    for piece in answer2:
        print("stream -> ", end="", flush=True)
    questions = [
        {"question": "What is HTML?"},
        {"question": "What is HTTP?"},
    ]

    # answer3 = chain.batch(questions)
    # print(answer3)
    for q, a in zip(questions, chain.batch(questions)):
        print(f"batch -> {q['question']:12} {a}")
    print()
