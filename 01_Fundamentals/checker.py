import ipaddress

while True:
# 1st ask user for an ip address
    ip_address = input("Write an IP address: ")
    clean_ip = ip_address.strip()
    if not clean_ip:
        print("Cannot leave a blank text. Try again")
        continue
    try:    
        ip = ipaddress.ip_address(clean_ip)
        print("IP address {ip} valid.")
        break
    except ValueError:
        print("The text is not a valid IP.")


