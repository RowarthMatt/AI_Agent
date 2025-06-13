import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    abs_working_directory = os.path.abspath(working_directory)
    join = os.path.join(working_directory, file_path)
    abs_file = os.path.abspath(join)
    if not abs_file.startswith(abs_working_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(join):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    file_content_string = ""

    try:
        with open(join, 'r') as f:
            file_content_string = f.read(MAX_CHARS)
    except Exception as e:
        return f"Error: cannot read file: {e}"
    
    if len(file_content_string) == MAX_CHARS:
        file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

    return file_content_string
