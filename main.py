"""Main agent runner file."""
import argparse
import os
import json

from dotenv import load_dotenv
from openai import OpenAI
from openai.types.chat import ChatCompletionMessageToolCallUnion, ChatCompletionMessage

from config import ToolResult
from functions import available_tools, function_map
from prompts import system_prompt
load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
BASE_URL = os.getenv("OPENROUTER_BASE_URL")

def construct_messages(message: str | ChatCompletionMessage, messages: list = []) -> list[dict[str, str]]:
    """Construct the message history for a session with latest message appended."""
    messages = [{"role": "system", "content": system_prompt}] if not messages else messages
    if isinstance(message, str):
        
        messages.append(
            {
                "role": "user",
                "content": message,
            }
        )
    else:
        message = message.model_dump() if isinstance(message, ChatCompletionMessage) else message
        messages.append(message)
    return messages

def call_tool(tool_call: ChatCompletionMessageToolCallUnion, verbose: bool = False) -> ToolResult:
    """Print tool call made by llm."""
    function_name = tool_call.function.name
    function_args = json.loads(tool_call.function.arguments or "{}")
    print(f"==={function_name}===")
    if verbose:
        print(f" - Calling function: {function_name}({function_args})")
    else:
        print(f" - Calling function: {function_name}")
    
    if function_name not in function_map:
        return ToolResult(
            tool_call_id= tool_call.id,
            content=f"Error: Unknown function: {function_name}"
        )
    function_args["cwd"] = "./calculator"
    result = function_map[function_name](**function_args)
    return ToolResult(
        tool_call_id=tool_call.id,
        content=result
    )

def main(message: str, verbose: bool) -> str:
    """Main agent runner function."""
    if not API_KEY:
        raise RuntimeError("API key not set. Please setup and Openrouter API key.")
    
    client = OpenAI(
        base_url=BASE_URL,
        api_key=API_KEY
    )
    messages = []
    for _ in range(20):
        messages = construct_messages(messages=messages, message=message) 
    
        response = client.chat.completions.create(
            model="openrouter/free",
            messages=messages,
            tools=available_tools,
        )
        if not response.usage:
            raise RuntimeError("Open-router API failed to respond.")

        if verbose:
            print(f"Prompt tokens: {response.usage.prompt_tokens}")
            print(f"Response tokens:{response.usage.completion_tokens}")
        message = response.choices[0].message
        messages = construct_messages(messages=messages, message=message.model_dump()) 
        if not message.tool_calls:
            print(f"AI: {message.content}")
            break
        
        for tool_call in message.tool_calls:
            tool_result = call_tool(tool_call=tool_call, verbose=verbose)
            if not tool_result.content:
                raise Exception("No Results form tool")
            if verbose:
                print(f"-> {tool_result.content}")
            messages.append(tool_result.model_dump())

            
    if verbose:
        for message in messages:
            print(f"{message["role"].title()} prompt:", message["content"])
            print("==="*2)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Agent.")
    parser.add_argument("message", type=str, help="message for the agent")
    parser.add_argument("--verbose", action="store_true", help="For details for the agents turn")
    args = parser.parse_args()

    main(message=args.message, verbose=args.verbose)

