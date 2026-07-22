"""
Project 01: Port Scanner Basic (Phase 1)

Checks TCP socket connections to identify open ports on a target host.
"""
import socket

def scan_port(ip, port):
    # Open TCP connection securely with "with"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1.0)  # Time limit (1 s)
        
        # connect_ex returns 0 if port is open
        result = s.connect_ex((ip, port))
        
        if result == 0:
            print(f"[+] El puerto {port} en {ip} está ABIERTO")
        else:
            print(f"[-] El puerto {port} en {ip} está CERRADO o FILTRADO")

