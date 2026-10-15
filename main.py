"""Main agent runner file."""
import argparse
import os

from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
BASE_URL = os.getenv("OPENROUTER_BASE_URL")

def construct_messages(message: str) -> list[dict[str, str]]:
    """Construct the message history for a session with latest message appended."""
    messages = [] # TODO: we add loading history later
    messages.append(
        {
            "role": "user",
            "content": message,
        }
    )
    return messages

def main(messages: list[str], verbose: bool) -> str:
    """Main agent runner function."""
    if not API_KEY:
        raise RuntimeError("API key not set. Please setup and Openrouter API key.")
    
    client = OpenAI(
        base_url=BASE_URL,
        api_key=API_KEY
    )
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
    )
    if not response.usage:
        raise RuntimeError("Open-router API failed to respond.")
    
    if verbose:
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens:{response.usage.completion_tokens}")
    return response.choices[0].message.content


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Agent.")
    parser.add_argument("message", type=str, help="message for the agent")
    parser.add_argument("--verbose", action="store_true", help="For details for the agents turn")
    args = parser.parse_args()

    verbose = args.verbose
    messages = construct_messages(message=args.message)
    
    if verbose:
        for message in messages:
            print(f"{message["role"].title()} prompt:", message["content"])
            print("==="*2)
    print("AI:", main(messages=messages, verbose=verbose))

