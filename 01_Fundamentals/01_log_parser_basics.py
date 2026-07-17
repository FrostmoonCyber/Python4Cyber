"""
Project 01: Log Parser Basics (Phase 1)

Parses authentication logs to filter and identify potential brute-force attacks.
"""
from pathlib import Path

route_log = Path("auth_log.txt")

fail_counter = 0
threshold = 5

# checking 1st the existence of the file
if route_log.exists():
    fail_counter = 0
    with open(route_log, "r", encoding="utf-8") as file:
        # check line by line the file 
        for line in file:
            if "FAILED" in line:
                print(line.strip())
                fail_counter += 1
               
# Show total counter
    print("-" * 40)
    print(f"[!] Complete Analysis. Total detected errors: {fail_counter}")
    # Alert brute force attack
    if fail_counter >= threshold:
        print("[CRITICAL] ALERT! Possible brute attack detected")
else:
    print("[-] The file does not exist.")