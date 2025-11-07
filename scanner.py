import socket
import sys
from datetime import datetime

def scan_port(target, port):
    """Scan a single port"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        
        result = sock.connect_ex((target, port))
        
        if result == 0:
            print(f"Port {port}: OPEN")
            return True
        
        sock.close()
        return False
        
    except socket.gaierror:
        print("Hostname could not be resolved")
        sys.exit()
    except socket.error:
        print("Could not connect to server")
        sys.exit()

def main():
    target = input("Enter target IP/hostname: ")
    
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("Hostname could not be resolved")
        sys.exit()
    
    print("-" * 50)
    print(f"Target: {target} ({target_ip})")
    print(f"Scan started at: {datetime.now()}")
    print("-" * 50)
    
    try:
        for port in range(1, 101):
            scan_port(target_ip, port)
    except KeyboardInterrupt:
        print("\n\nScan interrupted by user")
        sys.exit()
    
    print(f"\nScan completed at: {datetime.now()}")

if __name__ == "__main__":
    main()