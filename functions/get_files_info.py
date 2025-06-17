import os
from config import MAX_CHARS
from google.genai import types

def get_files_info(working_directory, directory=None):
    abs_working_directory = os.path.abspath(working_directory)
    abs_directory = abs_working_directory
    join = abs_working_directory
    if directory:
        join = os.path.join(working_directory, directory)
        abs_directory = os.path.abspath(join)
        if not abs_directory.startswith(abs_working_directory):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
    if not os.path.isdir(join):
        return f'Error: "{directory}" is not a directory'
    
    try:
        info = ""
        for file in os.listdir(join):
            path = os.path.join(join, file)
            size = os.path.getsize(path)
            is_dir = os.path.isdir(path)
            info += f"- {file}: file_size={size} bytes, is_dir={is_dir}\n"

        return info.strip()
    except Exception as e:
        return f"Error: listing files: {e}"
    
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
