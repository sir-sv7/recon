"""
Scanner functions for the Recon tool
"""

import socket
import dns.resolver
import requests
from colorama import Fore, Style
from ..core.config import COMMON_PORTS, PORT_SCAN_TIMEOUT, HTTP_TIMEOUT
from ..utils.utils import print_info, print_success, print_error

def scan_ports(target):
    """Scan common ports on the target."""
    open_ports = []
    print_info(f"Scanning {len(COMMON_PORTS)} ports...")
    
    for port, service in COMMON_PORTS.items():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(PORT_SCAN_TIMEOUT)
        result = sock.connect_ex((target, port))
        if result == 0:
            open_ports.append(f"{Fore.GREEN}[+] Port {port:5d} ({service:15}) is open{Style.RESET_ALL}")
        sock.close()
    
    return '\n'.join(open_ports) if open_ports else f"{Fore.RED}[!] No open ports found{Style.RESET_ALL}"

def resolve_ip(target):
    """Resolve IP to hostname or hostname to IP."""
    try:
        if '.' in target and target.replace('.', '').isdigit():
            try:
                hostname = socket.gethostbyaddr(target)[0]
                return f"{Fore.GREEN}[+] Hostname: {hostname}{Style.RESET_ALL}"
            except socket.herror:
                return f"{Fore.RED}[!] No hostname found for this IP{Style.RESET_ALL}"
        else:
            try:
                ip = socket.gethostbyname(target)
                return f"{Fore.GREEN}[+] IP Address: {ip}{Style.RESET_ALL}"
            except socket.gaierror:
                return f"{Fore.RED}[!] Could not resolve domain{Style.RESET_ALL}"
    except Exception as e:
        return f"{Fore.RED}[!] Error: {str(e)}{Style.RESET_ALL}"

def get_http_headers(target):
    """Get HTTP headers from the target."""
    try:
        if not target.startswith(('http://', 'https://')):
            target = 'https://' + target
            
        response = requests.get(target, timeout=HTTP_TIMEOUT)
        headers = response.headers
        
        result = []
        important_headers = ['server', 'x-powered-by', 'x-frame-options', 'content-type', 'strict-transport-security']
        
        for header in important_headers:
            if header in headers:
                result.append(f"{Fore.GREEN}[+] {header}: {headers[header]}{Style.RESET_ALL}")
                
        return '\n'.join(result) if result else f"{Fore.RED}[!] No important headers found{Style.RESET_ALL}"
    except Exception as e:
        return f"{Fore.RED}[!] Error: {str(e)}{Style.RESET_ALL}"

def enumerate_subdomains(domain):
    """Enumerate subdomains of the target domain."""
    subdomains = []
    common_subdomains = ['www', 'mail', 'ftp', 'localhost', 'webmail', 'smtp', 'pop', 'ns1', 'ns2', 'ns3', 'ns4']
    
    for subdomain in common_subdomains:
        try:
            full_domain = f"{subdomain}.{domain}"
            answers = dns.resolver.resolve(full_domain, 'A')
            for answer in answers:
                subdomains.append(f"{Fore.GREEN}[+] {full_domain} -> {answer}{Style.RESET_ALL}")
        except:
            continue
    
    return '\n'.join(subdomains) if subdomains else f"{Fore.RED}[!] No subdomains found{Style.RESET_ALL}"

def get_geoip(ip):
    """Get GeoIP information for the target IP."""
    try:
        response = requests.get(f'http://ip-api.com/json/{ip}')
        data = response.json()
        
        if data['status'] == 'success':
            result = []
            result.append(f"{Fore.GREEN}[+] Country: {data.get('country', 'N/A')}{Style.RESET_ALL}")
            result.append(f"{Fore.GREEN}[+] City: {data.get('city', 'N/A')}{Style.RESET_ALL}")
            result.append(f"{Fore.GREEN}[+] Region: {data.get('regionName', 'N/A')}{Style.RESET_ALL}")
            result.append(f"{Fore.GREEN}[+] ISP: {data.get('isp', 'N/A')}{Style.RESET_ALL}")
            result.append(f"{Fore.GREEN}[+] Timezone: {data.get('timezone', 'N/A')}{Style.RESET_ALL}")
            return '\n'.join(result)
        else:
            return f"{Fore.RED}[!] Could not get GeoIP information{Style.RESET_ALL}"
    except Exception as e:
        return f"{Fore.RED}[!] Error: {str(e)}{Style.RESET_ALL}" 