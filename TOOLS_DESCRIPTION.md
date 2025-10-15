# Deskripsi Tools MCP-Kali-Server

## 🔧 Tools yang Tersedia

### 1. **Nmap** - Network Scanner
**Deskripsi**: Tool untuk scanning jaringan dan port yang paling populer di dunia.

**Fungsi Utama**:
- Port scanning (TCP/UDP)
- Service detection
- OS fingerprinting
- Vulnerability detection
- Network mapping

**Contoh Penggunaan**:
```bash
# Basic port scan
nmap 192.168.1.1

# Service version detection
nmap -sV 192.168.1.1

# Scan specific ports
nmap -p 80,443,22,21 192.168.1.1

# Aggressive scan
nmap -A 192.168.1.1

# Scan entire subnet
nmap 192.168.1.0/24
```

**API Endpoint**: `POST /api/tools/nmap`

### 2. **Gobuster** - Directory/File Brute-forcer
**Deskripsi**: Tool untuk brute-force directories, files, DNS subdomains, dan virtual hosts.

**Fungsi Utama**:
- Directory brute-forcing
- File brute-forcing
- DNS subdomain enumeration
- Virtual host discovery
- Fast and efficient scanning

**Contoh Penggunaan**:
```bash
# Directory brute-forcing
gobuster dir -u http://target.com -w /usr/share/wordlists/dirb/common.txt

# DNS subdomain enumeration
gobuster dns -d target.com -w /usr/share/wordlists/dnsmap.txt

# Virtual host discovery
gobuster vhost -u http://target.com -w /usr/share/wordlists/vhosts.txt

# File brute-forcing
gobuster dir -u http://target.com -w /usr/share/wordlists/files.txt -x php,html,js
```

**API Endpoint**: `POST /api/tools/gobuster`

### 3. **Dirb** - Web Content Scanner
**Deskripsi**: Tool klasik untuk scanning konten web dan menemukan direktori tersembunyi.

**Fungsi Utama**:
- Web directory scanning
- File discovery
- Custom wordlist support
- Multiple output formats
- Recursive scanning

**Contoh Penggunaan**:
```bash
# Basic directory scan
dirb http://target.com

# Custom wordlist
dirb http://target.com /usr/share/wordlists/dirb/big.txt

# Specific extensions
dirb http://target.com -X .php,.html,.js

# Recursive scan
dirb http://target.com -r
```

**API Endpoint**: `POST /api/tools/dirb`

### 4. **Nikto** - Web Server Scanner
**Deskripsi**: Tool untuk scanning vulnerability web server yang komprehensif.

**Fungsi Utama**:
- Web server vulnerability scanning
- CGI vulnerability detection
- Outdated software detection
- Security misconfiguration detection
- Comprehensive reporting

**Contoh Penggunaan**:
```bash
# Basic web scan
nikto -h http://target.com

# Scan with specific port
nikto -h http://target.com -p 8080

# Scan with authentication
nikto -h http://target.com -id admin:password

# Output to file
nikto -h http://target.com -output nikto_results.txt
```

**API Endpoint**: `POST /api/tools/nikto`

### 5. **SQLMap** - SQL Injection Scanner
**Deskripsi**: Tool otomatis untuk mendeteksi dan mengeksploitasi SQL injection vulnerabilities.

**Fungsi Utama**:
- SQL injection detection
- Database fingerprinting
- Data extraction
- Database takeover
- Multiple database support

**Contoh Penggunaan**:
```bash
# Basic SQL injection test
sqlmap -u "http://target.com/page.php?id=1"

# POST data testing
sqlmap -u "http://target.com/login.php" --data="user=admin&pass=admin"

# Database enumeration
sqlmap -u "http://target.com/page.php?id=1" --dbs

# Table enumeration
sqlmap -u "http://target.com/page.php?id=1" -D database_name --tables
```

**API Endpoint**: `POST /api/tools/sqlmap`

### 6. **Metasploit** - Exploitation Framework
**Deskripsi**: Framework penetrasi testing yang paling populer untuk eksploitasi.

**Fungsi Utama**:
- Vulnerability exploitation
- Payload generation
- Post-exploitation modules
- Social engineering tools
- Comprehensive reporting

**Contoh Penggunaan**:
```bash
# Start Metasploit console
msfconsole

# Use exploit module
use exploit/windows/smb/ms17_010_eternalblue

# Set target
set RHOSTS 192.168.1.100

# Execute exploit
exploit
```

**API Endpoint**: `POST /api/tools/metasploit`

### 7. **Hydra** - Password Cracker
**Deskripsi**: Tool untuk brute-force attack pada berbagai protokol dan layanan.

**Fungsi Utama**:
- Password brute-forcing
- Multiple protocol support
- Parallel attacks
- Custom wordlists
- Fast and efficient

**Contoh Penggunaan**:
```bash
# SSH brute-force
hydra -l admin -P /usr/share/wordlists/rockyou.txt ssh://192.168.1.100

# FTP brute-force
hydra -L users.txt -P passwords.txt ftp://192.168.1.100

# HTTP form brute-force
hydra -l admin -P passwords.txt http-post-form://target.com/login.php:user=^USER^&pass=^PASS^:Invalid
```

**API Endpoint**: `POST /api/tools/hydra`

### 8. **John the Ripper** - Password Cracker
**Deskripsi**: Tool untuk cracking password hash yang powerful dan fleksibel.

**Fungsi Utama**:
- Hash cracking
- Multiple hash types
- Dictionary attacks
- Brute-force attacks
- Custom rules

**Contoh Penggunaan**:
```bash
# Basic hash cracking
john hashes.txt

# Wordlist attack
john --wordlist=/usr/share/wordlists/rockyou.txt hashes.txt

# Specific format
john --format=md5crypt hashes.txt

# Show cracked passwords
john --show hashes.txt
```

**API Endpoint**: `POST /api/tools/john`

### 9. **WPScan** - WordPress Scanner
**Deskripsi**: Tool khusus untuk scanning vulnerability WordPress.

**Fungsi Utama**:
- WordPress vulnerability scanning
- Plugin vulnerability detection
- Theme vulnerability detection
- User enumeration
- Password brute-forcing

**Contoh Penggunaan**:
```bash
# Basic WordPress scan
wpscan --url http://target.com

# User enumeration
wpscan --url http://target.com --enumerate u

# Plugin scan
wpscan --url http://target.com --enumerate p

# Password brute-force
wpscan --url http://target.com --passwords passwords.txt --usernames users.txt
```

**API Endpoint**: `POST /api/tools/wpscan`

### 10. **Enum4linux** - SMB/Windows Enumeration
**Deskripsi**: Tool untuk enumerasi informasi dari SMB dan Windows systems.

**Fungsi Utama**:
- SMB enumeration
- User enumeration
- Share enumeration
- Group enumeration
- Password policy detection

**Contoh Penggunaan**:
```bash
# Basic enumeration
enum4linux 192.168.1.100

# Aggressive enumeration
enum4linux -a 192.168.1.100

# User enumeration
enum4linux -U 192.168.1.100

# Share enumeration
enum4linux -S 192.168.1.100
```

**API Endpoint**: `POST /api/tools/enum4linux`

## 🚀 Generic Command Execution

Selain tools khusus di atas, MCP-Kali-Server juga mendukung eksekusi perintah umum melalui:

**API Endpoint**: `POST /api/command`

**Contoh Penggunaan**:
```bash
# System information
curl -X POST http://localhost:5000/api/command \
  -H "Content-Type: application/json" \
  -d '{"command": "whoami"}'

# Network scan
curl -X POST http://localhost:5000/api/command \
  -H "Content-Type: application/json" \
  -d '{"command": "ping -c 4 8.8.8.8"}'

# File operations
curl -X POST http://localhost:5000/api/command \
  -H "Content-Type: application/json" \
  -d '{"command": "ls -la /etc/passwd"}'
```

## 📊 Status Tools

Untuk mengecek status dan ketersediaan tools, gunakan:

**API Endpoint**: `GET /health`

Response akan menunjukkan status setiap tool:
```json
{
  "status": "healthy",
  "message": "Kali Linux Tools API Server is running",
  "tools_status": {
    "nmap": true,
    "gobuster": true,
    "dirb": true,
    "nikto": true
  },
  "all_essential_tools_available": true
}
```

## ⚠️ Catatan Penting

1. **Keamanan**: Semua tools ini dirancang untuk testing keamanan yang sah dan legal
2. **Izin**: Pastikan Anda memiliki izin sebelum melakukan scanning pada sistem yang bukan milik Anda
3. **Edukasi**: Gunakan tools ini untuk tujuan pembelajaran dan testing di lingkungan yang terkontrol
4. **Responsibility**: Pengguna bertanggung jawab penuh atas penggunaan tools ini

## 🔗 Integrasi dengan AI

MCP-Kali-Server memungkinkan integrasi dengan AI models seperti:
- Claude Desktop
- 5ire Desktop
- Custom MCP clients

AI dapat menggunakan tools ini untuk:
- Automated penetration testing
- CTF challenge solving
- Security assessment
- Vulnerability research
- Educational purposes
