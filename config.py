"""Configurations and constant for the agent and its harness."""
from pydantic import BaseModel
from typing import Literal

MAX_CHARACTERS = 10000

class ToolResult(BaseModel):
    """Schema for tool result after execution."""
    
    role: Literal["tool"] = "tool"
    tool_call_id: str
    content: str