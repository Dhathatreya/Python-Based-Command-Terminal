import os

def execute(args):
    """Creates a new directory."""
    if not args:
        print("mkdir: missing operand")
        return
    path = args[0]
    try:
        os.mkdir(path)
        print(f"Directory '{path}' created.")
    except FileExistsError:
        print(f"mkdir: cannot create directory '{path}': File exists")
    except Exception as e:
        print(f"mkdir: an error occurred: {e}")