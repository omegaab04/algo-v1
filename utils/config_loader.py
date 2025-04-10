import os
from datetime import datetime

LOG_FILE = "log.txt"

def log(msg: str):
    """Log message to console and file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    full_msg = f"[{timestamp}] {msg}"
    print(full_msg)

    with open(LOG_FILE, "a") as f:
        f.write(full_msg + "\n")