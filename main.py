"""Main agent runner file."""
import os

from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
BASE_URL = os.getenv("OPENROUTER_BASE_URL")

def main():
    """Main agent runner function."""
    if not API_KEY:
        raise RuntimeError("API key not set. Please setup and Openrouter API key.")
    
    client = OpenAI(
        base_url=BASE_URL,
        api_key=API_KEY
    )
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=[
            {
            "role": "user",
            "content": "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum"
            }
        ]
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    print(main())