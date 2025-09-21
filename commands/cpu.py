import psutil
import sys
import time
from datetime import datetime

def execute(args):
    """Displays real-time CPU usage."""
    try:
        print("Real-time CPU Usage (Press Ctrl+C to stop):")
        print("-" * 30)
        while True:
            usage = psutil.cpu_percent(interval=0.1)
            # Clear the current line and print new value
            sys.stdout.write(f"\rCPU Usage: {usage}%")
            sys.stdout.flush()
    except KeyboardInterrupt:
        print("\nReal-time monitoring stopped.")
        return
