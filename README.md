# TCP Port Scanner

A simple and effective TCP port scanner written in Python for security testing and network reconnaissance.

## Features
- TCP port scanning
- Multi-threading support
- Banner grabbing
- Customizable timeout
- JSON/CSV output

## Installation
```bash
git clone https://github.com/klavyeesir/tcp-port-scanner.git
cd tcp-port-scanner
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Usage
```bash
# Basic scan
python3 scanner.py

# With arguments (coming soon)
python3 scanner.py -t 192.168.1.1 -p 1-1000
```

## Requirements
- Python 3.8+
- colorama

## Disclaimer
This tool is for educational and authorized security testing purposes only. Always obtain proper authorization before scanning any network or system you do not own.

## License
MIT License

## Author
DevSecOps Portfolio Project
