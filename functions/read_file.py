"""Function to read contents of a file."""
import os

from config import MAX_CHARACTERS

def get_file_content(cwd: str, file_path: str) -> str:
    """Get the contents of the file if it exists in current working directory."""
    try:
        cwd_abs_path = os.path.abspath(cwd)
        target_file = os.path.normpath(os.path.join(cwd_abs_path, file_path))
        is_valid = os.path.commonpath((target_file, cwd_abs_path)) == cwd_abs_path
        if not is_valid:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        with open(target_file, "r") as f:
            content = f.read(MAX_CHARACTERS)
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARACTERS} characters]'
        return content
    except Exception as ex:
        return f"Error: {ex}"
