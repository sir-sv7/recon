# Recon 🔍

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue" alt="Python Version">
  <img src="https://img.shields.io/badge/License-MIT-green" alt="License">
  <img src="https://img.shields.io/badge/Version-1.1.0-orange" alt="Version">
</div>

<p align="center">
  Advanced Network Reconnaissance Tool
</p>

## 🌟 Features

- **IP/Domain Resolution**: Convert between IP addresses and domain names
- **Port Scanning**: Scan for open ports and identify services
- **Subdomain Enumeration**: Discover subdomains of target domains
- **HTTP Headers Analysis**: Extract and analyze HTTP headers
- **GeoIP Location**: Get geographical information for IP addresses
- **Multi-threaded Scanning**: Fast and efficient scanning
- **Beautiful CLI Interface**: Colorful and user-friendly output

## 📋 Requirements

- Python 3.8 or higher
- Required Python packages (automatically installed with pip):
  - requests
  - dnspython
  - colorama
  - python-whois
  - geoip2

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/sir-sv7/recon.git
cd recon
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## 💻 Usage

Run the tool:
```bash
python recon.py
```

Then follow the menu options:
1. Start Scan - Enter a domain or IP address to scan
2. Exit - Close the program

### Example Output

```
    ██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗
    ██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║
    ██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║
    ██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║
    ██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║
    ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝

=== Tool Information ===
Version: 1.1.0
Author: Anas
Description: Advanced Network Reconnaissance Tool
```

## 🔧 Features in Detail

### Port Scanning
- Scans common ports (20-27017)
- Identifies running services
- Fast and efficient scanning

### Subdomain Enumeration
- Checks common subdomain patterns
- Resolves subdomain IPs
- Identifies active subdomains

### HTTP Headers Analysis
- Extracts important security headers
- Shows server information
- Identifies web technologies

### GeoIP Information
- Country and city location
- ISP information
- Timezone data

## ⚠️ Disclaimer

This tool is for educational purposes only. Always ensure you have permission to scan the target system. The author is not responsible for any misuse or damage caused by this tool.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📧 Contact

Anas - [Linkedin](https://www.linkedin.com/in/anas-dev0)

Project Link: [https://github.com/sir-sv7/recon](https://github.com/sir-sv7/recon) 