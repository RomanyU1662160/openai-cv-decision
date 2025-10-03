import os
from dotenv import load_dotenv
from utils.get_pdf_content import get_pdf_content
from utils.prompt import build_prompt
from utils.setup_db import setup_database
from utils.setup_db import insert_user
from openai import OpenAI
from pydantic import BaseModel

load_dotenv()

open_api_key = os.getenv("OPENAI_API_KEY")

setup_database()
client = OpenAI()


class PDFSummarizer(BaseModel):
    name: str
    email: str
    skills: list[str]
    experiences: list[str]
    summary: str
    reasoning: list[str]


try:
    file_path = input("Enter the path to the PDF file: ")
    content = get_pdf_content(file_path)
    prompt = build_prompt(content)
    response = client.responses.parse(
        model="gpt-5-nano",
        input=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": content},
        ],
        text_format=PDFSummarizer,
    )
    print("Response from the model:")
    print(response.output_parsed)

    # Insert user data into the database
    parsed_data = response.output_parsed
    user_id = insert_user(
        name=parsed_data.name,
        email=parsed_data.email,
        skills=str(parsed_data.skills),  # Convert list to string for SQLite
        experiences=str(parsed_data.experiences),
        summary=parsed_data.summary,
        reasoning=str(parsed_data.reasoning)
    )
    print(f"User inserted with ID: {user_id}")

except Exception as e:
    print(f"Error: {e}")
