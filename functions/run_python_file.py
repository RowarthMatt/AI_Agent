import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path):
    abs_working_directory = os.path.abspath(working_directory)
    join = os.path.join(working_directory, file_path)
    abs_file = os.path.abspath(join)
    if not abs_file.startswith(abs_working_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(join):
        return f'Error: File "{file_path}" not found.'
    
    if file_path[-3:] != ".py":
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        result = subprocess.run(["python3", join], timeout=30, capture_output=True, text=True)
        stdout = f"STDOUT: {result.stdout}"
        stderr = f"STDERR: {result.stderr}"
        exit_code = result.returncode
        output = ""
        if result.stderr == "" and result.stdout == "":
            output = "No output produced"
        else:
            output = f"{stdout}\n{stderr}"
            if exit_code != 0:
                output += f"\nProcess exited with code {exit_code}"

        return output
    except Exception as e:
        return f'Error: cannot run "{file_path}" - {e}'
    
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file within the working directory and returns the output from the interpreter.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Optional arguments to pass to the Python file.",
                ),
                description="Optional arguments to pass to the Python file.",
            ),
        },
        required=["file_path"],
    ),
)
