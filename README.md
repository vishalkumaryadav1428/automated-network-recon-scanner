# 🚀 Automated Reconnaissance & Nmap Scanner

An efficient, Python-based network automation tool designed to streamline the reconnaissance phase of penetration testing. This script utilizes the `python-nmap` library to perform rapid, comprehensive port scanning, service version detection, and vulnerability identification.

## ✨ Features
* **Aggressive Scanning:** Utilizes Nmap's `-T4` timing template for fast execution.
* **Comprehensive Enumeration:** Runs default Nmap Scripting Engine (NSE) scripts (`-sC`) and detects service versions (`-sV`).
* **Ping Bypass:** Uses `-Pn` to treat all hosts as online, effectively bypassing endpoints that block ICMP ping probes.
* **Structured Output:** Parses complex raw Nmap data into a clean, readable console format for quick analysis.
* **Cross-Platform:** Works seamlessly on both Windows and Linux environments.

## 🛠️ Prerequisites
Before running this tool, ensure you have the following installed:
1. **Python 3.x**
2. **Nmap Network Scanner:** * **Windows:** Download and install from [Nmap.org](https://nmap.org/download.html) (Ensure it's added to your system PATH).
   * **Linux (Kali/Ubuntu):** `sudo apt install nmap`

## ⚙️ Installation

1. Clone this repository to your local machine:
   ```bash
   git clone [https://github.com/YourUsername/Automated-Scanner.git](https://github.com/YourUsername/Automated-Nmap-Scanner.git)
   cd Automated-Scanner

2. Install the required Python dependencies:

Bash

pip install python-nmap


🚀 Usage
Run the script from your terminal or command prompt:

Bash

python scanner.py


When prompted, enter the target IP address or domain name (e.g., scanme.nmap.org):

Enter the target IP or Domain: scanme.nmap.org

[+] Starting Fast & Comprehensive Scan on: scanme.nmap.org
[+] Running Default Scripts (-sC) and Version Detection (-sV)...
[+] Please wait, gathering data...



⚠️ Disclaimer
For Educational and Authorized Testing Purposes Only. Scanning networks or hosts without explicit, written permission is illegal. The author is not responsible for any misuse or damage caused by this tool. Always ensure you have the proper authorization (Rules of Engagement) before conducting any security assessments.
