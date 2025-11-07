"""
Configuration file for TCP Port Scanner
"""

# Default settings
DEFAULT_TIMEOUT = 1.0
DEFAULT_THREADS = 100
DEFAULT_PORT_RANGE = (1, 1024)

# Common ports to scan
COMMON_PORTS = {
    20: "FTP Data",
    21: "FTP Control",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    8080: "HTTP Proxy",
}

# Banner grabbing settings
BANNER_TIMEOUT = 2.0
BANNER_BUFFER_SIZE = 1024
