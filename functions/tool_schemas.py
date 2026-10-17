"""Define the functions as tool in OPENAI SDK format."""
from openai.types import FunctionDefinition

schema_get_files_info = {
    "type": "function",
    "function": FunctionDefinition(
        name="get_files_info",
        description="Lists files in a specified directory parameter relative to the working directory, \
            providing file size and directory status",
        parameters={
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from,\
                        relative to the working directory (default is the working directory itself)",
                },
            },
        }
        
    ).model_dump()
}

schema_get_file_content = {
    "type": "function",
    "function": FunctionDefinition(
        name="get_file_content",
        description="Read the contents of the file path relative to the working directory.",
        parameters={
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path of the file, to read, relative to cwd \
                    (default is the working directory itself)",
                },
            },
        }
        
    )
}

schema_write_file = {
    "type": "function",
    "function": FunctionDefinition(
        name="write_file",
        description="Write/overwrite contents of the file on the provided file path relative to the working directory.",
        parameters={
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path of the file to write content for (default cwd is handled by tool)",
                },
                "content": {
                    "type": "string",
                    "description": "Content of the file",
                },
            },
        }
        
    )
}

schema_run_python_file = {
    "type": "function",
    "function": FunctionDefinition(
        name="run_python_file",
        description="Run a specific python file and return its results (default cwd is handled by tool)",
        parameters={
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Python file to run.",
                },
                "args": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Additional optional arguments for the run command for the python file."
                }
            },
        }
        
    )
}