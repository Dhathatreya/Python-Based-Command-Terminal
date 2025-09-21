import os

def execute(args):
    """Changes the current directory."""
    if not args:
        print("cd: missing operand")
        return
    path = args[0]
    try:
        os.chdir(path)
    except FileNotFoundError:
        print(f"cd: no such file or directory: {path}")
    except Exception as e:
        print(f"cd: an error occurred: {e}")