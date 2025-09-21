import os

def execute(args):
    """Removes a file or empty directory."""
    if not args:
        print("rm: missing operand")
        return
    path = args[0]
    try:
        if os.path.isfile(path):
            os.remove(path)
            print(f"Removed file: '{path}'")
        elif os.path.isdir(path):
            os.rmdir(path)
            print(f"Removed directory: '{path}'")
    except FileNotFoundError:
        print(f"rm: cannot remove '{path}': No such file or directory")
    except OSError:
        print(f"rm: cannot remove '{path}': Directory not empty")
    except Exception as e:
        print(f"rm: an error occurred: {e}")