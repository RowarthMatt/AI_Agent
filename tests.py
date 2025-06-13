from functions.get_files_info import get_files_info 
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

def tests():
    print("\n------------------------------\nTEST 1")
    print(run_python_file("calculator", "main.py"))
    print("\n------------------------------\nTEST 2")
    print(run_python_file("calculator", "tests.py"))
    print("\n------------------------------\nTEST 3")
    print(run_python_file("calculator", "../main.py"))
    print("\n------------------------------\nTEST 4")
    print(run_python_file("calculator", "nonexistent.py"))



if __name__ == "__main__":
    tests()