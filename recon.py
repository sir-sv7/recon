#!/usr/bin/env python3
"""
Recon - Advanced Network Reconnaissance Tool
"""

import threading
import time
from colorama import Fore, Style, init
from src.core.config import TOOL_NAME, VERSION, AUTHOR, DESCRIPTION
from src.scanners.scanners import (
    resolve_ip,
    scan_ports,
    enumerate_subdomains,
    get_http_headers,
    get_geoip
)
from src.utils.utils import print_success, print_error, print_info, print_section

init(autoreset=True)

LOGO = fr"""{Fore.CYAN}
    ██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗
    ██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║
    ██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║
    ██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║
    ██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║
    ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝
{Style.RESET_ALL}"""

def display_welcome():
    """Display welcome message and tool information."""
    print(LOGO)
    print_section("Tool Information")
    print(f"{Fore.CYAN}Version: {Fore.WHITE}{VERSION}")
    print(f"{Fore.CYAN}Author: {Fore.WHITE}{AUTHOR}")
    print(f"{Fore.CYAN}Description: {Fore.WHITE}{DESCRIPTION}")
    print(f"\n{Fore.YELLOW}Use this tool responsibly and only on systems you own or have permission to scan.{Style.RESET_ALL}")

def display_menu():
    """Display the main menu."""
    print_section("Available Options")
    print(f"{Fore.GREEN}[1] Start Scan")
    print(f"{Fore.RED}[2] Exit{Style.RESET_ALL}")

def display_progress(message):
    """Display a progress message with animation."""
    chars = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    for char in chars:
        print(f"\r{Fore.YELLOW}[{char}] {message}{Style.RESET_ALL}", end="", flush=True)
        time.sleep(0.1)
    print("\r" + " " * (len(message) + 10), end="\r")

def run_scan(target):
    """Run all scans on the target."""
    print_info(f"Starting scan for: {target}")
    
    results = {}
    threads = []
    completed_scans = 0
    total_scans = 4  # Total number of scans
    
    # Define scan functions
    scans = {
        'IP Resolution': lambda: resolve_ip(target),
        'Port Scan': lambda: scan_ports(target),
        'Subdomains': lambda: enumerate_subdomains(target),
        'HTTP Headers': lambda: get_http_headers(target)
    }
    
    # Run scans in threads
    for name, func in scans.items():
        thread = threading.Thread(target=lambda: results.update({name: func()}))
        threads.append(thread)
        thread.start()
        display_progress(f"Running {name}...")
        completed_scans += 1
        print_info(f"Progress: {completed_scans}/{total_scans} scans completed")
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    # Get GeoIP if target is an IP
    if '.' in target and target.replace('.', '').isdigit():
        display_progress("Getting GeoIP information...")
        results['GeoIP'] = get_geoip(target)
    
    # Display results
    print_section("SCAN RESULTS")
    
    # Display target information first
    print_section("Target Information")
    print(f"{Fore.GREEN}[+] Domain/IP: {target}{Style.RESET_ALL}")
    
    # Display IP/Domain resolution if available
    if 'IP Resolution' in results:
        print_section("Resolution Information")
        print(results['IP Resolution'])
    
    # Display other results
    for name, result in results.items():
        if name not in ['IP Resolution']:
            print_section(name)
            print(result)
    
    print_section("Scan Complete")
    print_success("Scan completed successfully!")
    print(f"{Fore.YELLOW}Total scans completed: {completed_scans}{Style.RESET_ALL}")

def main():
    """Main function."""
    display_welcome()
    while True:
        display_menu()
        choice = input(f"\n{Fore.YELLOW}Enter your choice: {Style.RESET_ALL}")
        
        if choice == '1':
            target = input(f"{Fore.YELLOW}Enter domain or IP address: {Style.RESET_ALL}")
            if target.strip():
                run_scan(target.strip())
                break
            else:
                print_error("Please enter a valid domain or IP address")
        elif choice == '2':
            print_error("Exiting...")
            break
        else:
            print_error("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
