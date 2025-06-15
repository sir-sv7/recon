"""
Configuration settings for the Recon tool
"""

# Tool Information
TOOL_NAME = "Recon"
VERSION = "1.1.0"
AUTHOR = "Anas"
DESCRIPTION = "Advanced Network Reconnaissance Tool"

# Colors
COLORS = {
    'info': '\033[94m',    # Blue
    'success': '\033[92m', # Green
    'warning': '\033[93m', # Yellow
    'error': '\033[91m',   # Red
    'reset': '\033[0m'     # Reset
}

# Scanner Settings
PORT_SCAN_TIMEOUT = 1
HTTP_TIMEOUT = 5
DNS_TIMEOUT = 3

# Common Ports
COMMON_PORTS = {
    20: "FTP-DATA",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    465: "SMTPS",
    587: "Submission",
    993: "IMAPS",
    995: "POP3S",
    1433: "MSSQL",
    1434: "MSSQL-UDP",
    1521: "Oracle",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    6379: "Redis",
    8080: "HTTP-Proxy",
    8443: "HTTPS-Alt",
    8888: "HTTP-Alt",
    9000: "Jenkins",
    9090: "HTTP-Alt",
    27017: "MongoDB"
} 