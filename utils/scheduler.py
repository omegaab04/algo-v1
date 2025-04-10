import time
from datetime import datetime

def wait_until(target_hour: int, target_minute: int):
    """Sleep until target market open (e.g. 9:30am)."""
    while True:
        now = datetime.now()
        if now.hour == target_hour and now.minute == target_minute:
            break
        print(f"⏳ Waiting for market open... {now.strftime('%H:%M:%S')}")
        time.sleep(30)