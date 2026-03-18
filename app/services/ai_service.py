import os
from openai import OpenAI
from app.utils.enums import Priority
from app.config import API_KEY
import logging
api_key = API_KEY

if not api_key:
    raise ValueError("OpenRouter API key not found. Please set OPENROUTER_API_KEY in your .env file.")

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=api_key,
)

#Logging for better debugging
logging.info("AI service Initialization")

logging.info("Generating description...")
def generate_description(title: str) -> str:
    response = client.chat.completions.create(
        model="arcee-ai/trinity-large-preview:free",
        messages=[
            {
                "role": "user",
                "content": f"Generate a short 40-60 word description for this task: {title}"
            }
        ],
        extra_body={"reasoning": {"enabled": False}}
    )
    return response.choices[0].message.content

logging.info("Description Generated.")

logging.info("Declaring Priority...")
def suggest_priority(title: str, description: str) -> Priority:
    response = client.chat.completions.create(
        model="arcee-ai/trinity-large-preview:free",
        messages=[
            {
                "role": "user",
                "content": f"""
                Title: {title}
                Description: {description}

                Assign priority: LOW, MEDIUM, or HIGH.
                Return ONLY the word.
                """
            }
        ],
        extra_body = {"reasoning": {"enabled": False}}
    )

    priority_str = response.choices[0].message.content.strip().upper()

    mapping = {
        "LOW": Priority.low,
        "MEDIUM": Priority.medium,
        "HIGH": Priority.high
    }
    logging.info(f"Priority Declared. Set to: {mapping.get(priority_str, Priority.medium)}")
    return mapping.get(priority_str, Priority.medium)