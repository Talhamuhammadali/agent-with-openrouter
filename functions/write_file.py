"""Function to read contents of a file."""
import os

from config import MAX_CHARACTERS

def write_file(cwd: str, file_path: str, content: str) -> str:
    """Get the contents of the file if it exists in current working directory."""
    try:
        cwd_abs_path = os.path.abspath(cwd)
        target_file = os.path.normpath(os.path.join(cwd_abs_path, file_path))
        is_valid = os.path.commonpath((target_file, cwd_abs_path)) == cwd_abs_path
        if not is_valid:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        if os.path.isdir(target_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        os.makedirs(os.path.dirname(target_file), exist_ok=True)

        with open(target_file, "w") as f:
            f.write(content)
            
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as ex:
        return f"Error: {ex}"
