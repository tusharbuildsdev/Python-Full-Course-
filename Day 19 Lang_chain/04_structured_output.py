
from dotenv import load_dotenv
import os

from pydantic import BaseModel, Field
from langchain_core.output_parsers import JsonOutputParser
from langchain_groq import ChatGroq

load_dotenv()

MODEL = "llama-3.1-8b-instant"

class MovieReview(BaseModel):
    """A structured summary of a movie review."""
    title: str = Field(description="the movie's title")
    sentiment: str = Field(description="one of: positive, negative, mixed")
    rating: int = Field(description="a score from 1 to 10")
    reasons: list[str] = Field(description="short bullet reasons for the rating")

if not os.getenv("GROQ_API_KEY"):
    print("No API Key")

else:
    model = ChatGroq(model=MODEL, temperature=0)
    review_text  = (
        "I finally watched Intersteller. The Visuals and score was amazing " "through the middle draged little "

    )
    structured = model.with_structured_output(MovieReview)
    result = structured.invoke(f"Extract a structured review from:\n{review_text}")
    print(result)