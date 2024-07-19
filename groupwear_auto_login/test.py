import os

def get_current_directory():
    return os.path.dirname(os.path.abspath(__file__))

current_path = get_current_directory()

print(current_path)