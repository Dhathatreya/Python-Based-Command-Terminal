import os

def execute(args):
    """Lists contents of the current directory."""
    try:
        for item in os.listdir('.'):
            print(item)
    except Exception as e:
        print(f"ls: an error occurred: {e}")