import psutil

def execute(args):
    """Lists running processes."""
    print(f"{'PID':>5} {'Name'}")
    print("-" * 20)
    for count, process in enumerate(psutil.process_iter(['pid', 'name'])):
        if count >= 15:
            break
        print(f"{process.info['pid']:>5} {process.info['name']}")