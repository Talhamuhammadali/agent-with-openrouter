"""Main agent runner file."""
import argparse
import os

from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
BASE_URL = os.getenv("OPENROUTER_BASE_URL")

def main(message: str) -> str:
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
            "content": message,
            }
        ]
    )
    if not response.usage:
        raise RuntimeError("Open-router API failed to respond.")
    
    print(f"Prompt tokens: {response.usage.prompt_tokens}")
    print(f"Response tokens:{response.usage.completion_tokens}")
    return response.choices[0].message.content


if __name__ == "__main__":
    message = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum"
    parser = argparse.ArgumentParser(description="Simple Agent.")
    parser.add_argument("message", type=str, help="message for the agent")
    args = parser.parse_args()
    message = args.message
    print("Human:", message)
    print("==="*2)
    print("AI:", main(message=message))
