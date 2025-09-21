import psutil
import sys
import time

def execute(args):
    """Displays real-time memory usage."""
    try:
        print("Real-time Memory Usage (Press Ctrl+C to stop):")
        print("-" * 40)
        while True:
            memory = psutil.virtual_memory()
            total_gb = memory.total / (1024 ** 3)
            available_gb = memory.available / (1024 ** 3)
            # Clear the current line and print new values
            sys.stdout.write(f"\rMemory Usage: {memory.percent}% | Total: {total_gb:.2f} GB | Available: {available_gb:.2f} GB")
            sys.stdout.flush()
    except KeyboardInterrupt:
        print("\nReal-time monitoring stopped.")
        return
