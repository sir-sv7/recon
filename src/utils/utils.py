"""
Utility functions for the Recon tool
"""

import socket
from colorama import Fore, Style
from ..core.config import COLORS

def is_valid_ip(ip):
    """Check if the given string is a valid IP address."""
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

def is_valid_domain(domain):
    """Check if the given string is a valid domain name."""
    try:
        socket.gethostbyname(domain)
        return True
    except socket.error:
        return False

def print_success(message):
    """Print a success message."""
    print(f"{Fore.GREEN}[+] {message}{Style.RESET_ALL}")

def print_error(message):
    """Print an error message."""
    print(f"{Fore.RED}[!] {message}{Style.RESET_ALL}")

def print_info(message):
    """Print an info message."""
    print(f"{Fore.YELLOW}[*] {message}{Style.RESET_ALL}")

def print_section(title):
    """Print a section title."""
    print(f"\n{Fore.CYAN}{title}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}{'='*50}{Style.RESET_ALL}") 