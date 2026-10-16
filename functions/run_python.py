"""Function that runs the provided python file."""
import os
import subprocess

def run_python_file(cwd: str, file_path: str, args: list[str] | None = None) -> str: 
    """Run a python file with provided commands."""
    try:
        cwd_abs_path = os.path.abspath(cwd)
        target_file = os.path.normpath(os.path.join(cwd_abs_path, file_path))
        is_valid = os.path.commonpath((target_file, cwd_abs_path)) == cwd_abs_path
        if not is_valid:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        command = ["python", target_file]
        if args:
            command.extend(args)
        output = subprocess.run(command, cwd=cwd_abs_path, capture_output=True, text=True, timeout=30)
    
        response = ""
        if output.returncode > 0:
            response += f"Process exited with code {output.returncode}"
        if not output.stderr and not output.stdout:
            response += "No output produced"
        else:
            response += f"STDOUT: {output.stdout}\nSTDERR: {output.stderr}"
        return response
    except Exception as ex:
        return f"Error: executing Python file: {ex}"

