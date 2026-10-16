"""Function to list directory's contents."""

import os

from typing import TypedDict

class FsItem(TypedDict):
    """Record of a filesystem item."""
    name: str
    file_size: int
    is_dir: bool

def render_fs_item(item: FsItem) -> str:
    """Render the provided file system item."""
    return f"- {item.get("name")}: file_size={item.get("file_size")}, is_dir={item.get("is_dir")}"

def get_file_info(working_directory: str, directory: str = ".") -> str:
    """List contents of the current working directory."""
    try:
        base_response = "Result for current directory:\n"
                
        cwd_abs_path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(cwd_abs_path, directory))
        if not os.path.isdir(target_dir):
            return base_response + f'\tError: "{directory}" is not a directory'

        is_valid = cwd_abs_path == os.path.commonpath((target_dir, cwd_abs_path))
        
        if not is_valid:
            return base_response + f'\tError: Cannot list "{directory}" as it is outside the permitted working directory'

        dir_renders = []
        for item in os.listdir(target_dir):
            item_path = os.path.join(target_dir, item)
            item = FsItem(
                name=item,
                file_size=os.path.getsize(item_path),
                is_dir=os.path.isdir(item_path)   
            )
            dir_renders.append(render_fs_item(item=item))
        
        
        return base_response + "\n".join(dir_renders)
    except Exception as ex:
        return f"Error: {ex}"