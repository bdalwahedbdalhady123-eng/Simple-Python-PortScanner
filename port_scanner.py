import socket
import sys
from datetime import datetime

target_host = input("Enter host to scan (e.g., 127.0.0.1): ")

try:
    target_ip = socket.gethostbyname(target_host)
except socket.gaierror:
    print("\n Hostname could not be resolved. Exiting.")
    sys.exit()

print("-" * 50)
print(f"Scanning Target: {target_ip}")
print(f"Time Started: {str(datetime.now())}")
print("-" * 50)

ports_to_scan = [21, 22, 23, 25, 80, 110, 443, 8080]

try:
    for port in ports_to_scan:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0)
        result = s.connect_ex((target_ip, port))
        if result == 0:
            print(f"Port {port}: OPEN")
        else:
            print(f"Port {port}: Closed")
        s.close()

except KeyboardInterrupt:
    print("\n Exiting script.")
    sys.exit()

except socket.error:
    print("\n Could not connect to server.")
    sys.exit()
