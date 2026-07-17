"""
Project 01: IP Format Checker (Phase 1)
Validates IPv4 addresses to ensure correct formatting before processing network operations.

"""

import ipaddress

while True:
# 1st ask user for an ip address
    ip_address = input("Write an IP address: ")
    clean_ip = ip_address.strip()               
    if not clean_ip:                            #check if user text has blank spaces
        print("Cannot leave a blank text. Try again") 
        continue
    try:    
        ip = ipaddress.ip_address(clean_ip)     #check if IP format is valid
        print("IP address {ip} valid.")
        break
    except ValueError:
        print("The text is not a valid IP.")


