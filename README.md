<div align="center">
  <h1> Advanced Nmap Network Scanning & Vulnerability Analysis Guide</h1>
  
  ![Nmap](https://img.shields.io/badge/Tool-Nmap-blue.svg)
  ![OS](https://img.shields.io/badge/OS-Kali%20Linux-black.svg)
  ![Security](https://img.shields.io/badge/Focus-Cybersecurity-red.svg)
</div>

---

##  Project Overview
This project documents the comprehensive use of **Nmap (Network Mapper)** for network infrastructure mapping, service enumeration, and potential vulnerability identification. The guide covers a wide spectrum of techniques, ranging from basic host discovery to advanced IDS/IPS evasion strategies.

---

##  1. Network Discovery & Scanning Strategies

A comparison of fundamental commands used to map the status of targets on a network:

| Command | Scan Type | Description | Stealth Level |
| :--- | :--- | :--- | :--- |
| `nmap -sS [IP]` | **TCP SYN (Stealth)** | Half-open scan. Does not complete the 3-way handshake. | High |
| `nmap -sT [IP]` | **TCP Connect** | Full connection. Easily logged by target systems. | Low |
| `nmap -sU [IP]` | **UDP Scan** | Scans UDP-based services like DNS, SNMP, and DHCP. | Medium |
| `nmap -sn [IP/24]` | **Ping Sweep** | Discovers active hosts on the network without port scanning. | High |

---

##  2. Deep Enumeration: OS & Service Detection

Understanding the underlying technologies behind open ports is a critical step:
* **`nmap -sV --version-intensity 5 [IP]`** : Aggressively determines the exact version numbers of services running on open ports.
* **`nmap -O --osscan-guess [IP]`** : Attempts to guess the target's operating system by analyzing the TCP/IP stack footprint.
* **`nmap -A [IP]`** : **Aggressive Scan.** Combines OS detection, version scanning, script scanning, and traceroute into a single command.

---

##  3. Nmap Scripting Engine (NSE) for Vulnerability Hunting

Utilizing Nmap's embedded scripting engine to transform it into a vulnerability scanner:
* **`nmap -sC [IP]`** : Runs a collection of default, safe scripts for basic enumeration.
* **`nmap --script vuln [IP]`** : Scans the target directly for known vulnerabilities (CVEs).
* **`nmap --script smb-enum-users,smb-enum-shares [IP]`** : Enumerates usernames and shared directories over the SMB protocol.

---

##  4. Firewall & IDS/IPS Evasion Techniques

Advanced methodologies used to bypass security appliances or obscure scan traffic:
* **`nmap -f [IP]`** : **Packet Fragmentation.** Splits packets into smaller 8-byte fragments to bypass simple firewalls.
* **`nmap -D RND:10 [IP]`** : **Decoy Scan.** Cloaks your real IP address by generating 10 random decoy IP addresses in the target's logs.
* **`nmap --spoof-mac 0 [IP]`** : Spoofs the MAC address to a completely random one, ensuring stealth on local networks.

---

##  5. Output & Reporting

Properly documenting scan results is essential for security analysis:
* `nmap -oN scan_report.txt [IP]` : Saves results in a standard, human-readable text format.
* `nmap -oX scan_report.xml [IP]` : Saves results in XML format (required for importing into tools like Metasploit).
* `nmap -oG scan_report.gnmap [IP]` : Saves results in a "Greppable" format for easy terminal parsing.

---

##  References & Appendix

The following academic and technical resources were referenced during the research, execution, and reporting phases of this project:

1. **Official Nmap Documentation:** Gordon "Fyodor" Lyon, *Nmap Network Scanning*. ([nmap.org](https://nmap.org/book/man.html))
2. **Nmap Scripting Engine (NSE):** Script methodologies and vulnerability references. ([nmap.org/nsedoc](https://nmap.org/nsedoc/))
3. **SANS Institute:** Nmap Cheat Sheet and evasion methodologies.
4. **Test Environment & Attachments:** 
   * All attachments and scan outputs included in this project were generated through isolated tests conducted on a **Kali Linux** virtual machine within a local lab environment.

---

##  Disclaimer
This project and its documentation are strictly for **educational and academic research purposes**. The tools and techniques demonstrated here were used solely on authorized target systems within an isolated laboratory environment. Unauthorized network scanning is illegal. The author assumes no liability for the misuse of this information.

