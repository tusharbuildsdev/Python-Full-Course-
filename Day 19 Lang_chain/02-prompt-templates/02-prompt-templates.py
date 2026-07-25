from dotenv import load_dotenv
import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

load_dotenv()
MODEL = "llama-3.1-8b-versatile"
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a translator. Translate the text into {language}. Reply with only the translation.",
        ),
        ("human", "{text}"),
    ]
)
print("Template variables it expects:", prompt.input_variables)
print()
messages = prompt.format_messages(language="French", text="Good morning, friends!")
if not os.getenv("GROQ_API_KEY"):
    print("No API KEY")
else:
    model = ChatGroq(model=MODEL, temperature=0)
    reply = model.invoke(messages)
    print("Model translation (French):", reply.content)
