import time

# Simulated correct password (for educational purposes only)
CORRECT_PASSWORD = "Secure123!"

# Load wordlist
try:
    with open("wordlist.txt", "r") as file:
        passwords = file.read().splitlines()
except FileNotFoundError:
    print("Wordlist file not found.")
    exit()

print("Starting brute force attack simulation...\n")
time.sleep(1)

attempts = 0
MAX_ATTEMPTS = 20  # Simulated rate limiting

for password in passwords:
    attempts += 1
    print(f"Trying password: {password}")
    time.sleep(0.3)  # Simulate delay between attempts

    if password == CORRECT_PASSWORD:
        print(f"\n[+] Password found: {password}")
        print(f"Attempts: {attempts}")
        break

    if attempts >= MAX_ATTEMPTS:
        print("\n[-] Account locked due to too many attempts!")
        break
else:
    print("\n[-] Password not found in wordlist")
