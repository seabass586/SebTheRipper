import hashlib
import requests 
import threading
import time
import queue

# Define constants
DEFAULT_WORDLIST_URL = "https://raw.githubusercontent.com/berzerk0/Probable-Wordlists/master/Real-Passwords/Top12Thousand-probable-v2.txt"
THREAD_COUNT = 10  # Number of threads to use

# Create a queue for passwords
password_queue = queue.Queue()

def read_wordlist(url):
    """Fetch the wordlist from a URL and process it line by line."""
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        print("[*] Fetching wordlist...")
        for line in response.iter_lines(decode_unicode=True):
            if line:
                password_queue.put(line.strip())
    except requests.RequestException as e:
        print(f"[!] Error fetching wordlist: {e}")

def hash_password(password):
    """Hash a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def brute_force_worker(actual_hash, found_flag):
    """Worker function for multi-threaded brute-force attack."""
    while not password_queue.empty() and not found_flag[0]:
        guess = password_queue.get()
        if hash_password(guess) == actual_hash:
            found_flag[0] = True
            print(f"\nPassword cracked: {guess} \nChange it immediately!\n")
            break
        password_queue.task_done()

def start_brute_force(actual_hash):
    """Start the brute-force attack using multi-threading."""
    found_flag = [False]  # Shared variable across threads
    threads = []

    print(f"[*] Starting brute-force attack with {THREAD_COUNT} threads...\n")

    for _ in range(THREAD_COUNT):
        thread = threading.Thread(target=brute_force_worker, args=(actual_hash, found_flag))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    if not found_flag[0]:
        print("Password NOT found in wordlist. Good security!")

if __name__ == "__main__":
    # Get user input for password
    print("\n[*] Enter a password to test its strength:")
    actual_password = input().strip()
    actual_password_hash = hash_password(actual_password)

    # Get wordlist URL (default or custom)
    print("\n[*] Press Enter to use the default wordlist or enter a custom wordlist URL:")
    custom_url = input().strip()
    wordlist_url = custom_url if custom_url else DEFAULT_WORDLIST_URL

    start_time = time.time()  # Start timing

    # Fetch wordlist
    read_wordlist(wordlist_url)

    # Start brute force attack
    start_brute_force(actual_password_hash)

    # Display execution time
    end_time = time.time()
    print(f"\nExecution Time: {end_time - start_time:.2f} seconds")
