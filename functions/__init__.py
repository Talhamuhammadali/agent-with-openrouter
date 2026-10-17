"""Functions module."""

from collections.abc import Callable

from functions.tool_schemas import *
from functions.list_files import get_file_info
from functions.read_file import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file


available_tools = [
    schema_get_files_info,
    schema_get_file_content,
    schema_write_file,
    schema_run_python_file
]

function_map: dict[str, Callable[..., str]] = {
    "get_file_content": get_file_content,
    "get_files_info": get_file_info,
    "write_file": write_file,
    "run_python_file": run_python_file,
    
}