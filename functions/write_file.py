import os

def write_file(working_directory, file_path, content):
    abs_working_directory = os.path.abspath(working_directory)
    join = os.path.join(working_directory, file_path)
    abs_file_path = os.path.abspath(join)

    if not abs_file_path.startswith(abs_working_directory):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    dir = os.path.dirname(abs_file_path)

    if os.path.exists(abs_file_path) and os.path.isdir(abs_file_path):
        return f'Error: "{file_path}" is a directory, not a file'

    if not os.path.exists(dir):
        os.makedirs(dir)

    try:
        with open(abs_file_path, "w") as f:
            f.write(content)
    except Exception as e:
        return f'Error: cannot write to "{file_path}"'
    
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'