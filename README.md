<<<<<<< HEAD
# MCP-Kali-Server

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Ready-brightgreen.svg)]()

**MCP-Kali-Server** adalah jembatan API ringan yang menghubungkan klien Model Context Protocol (MCP) seperti Claude Desktop dan 5ire ke mesin Kali Linux. Tool ini memungkinkan penetrasi testing berbantuan AI dengan menjalankan perintah terminal langsung dari klien MCP.

## 🚀 Fitur Utama

- **🧠 AI Endpoint Integration**: Menghubungkan klien MCP ke berbagai model AI
- **🖥️ Command Execution API**: API terkontrol untuk menjalankan perintah terminal di Kali Linux
- **🕸️ Web Challenge Support**: AI dapat berinteraksi dengan aplikasi web, menangkap flag, dan melakukan tugas menggunakan tools seperti `curl`, `wget`, dan `gobuster`
- **🔐 Dirancang untuk Profesional Keamanan**: Ideal untuk red teamers, bug bounty hunters, dan pemain CTF
- **⚡ Real-time Execution**: Eksekusi perintah secara real-time dengan output streaming
- **🛡️ Security Focused**: Dibangun khusus untuk offensive security testing

## 📋 Tools yang Didukung

### Network Scanning
- **Nmap** - Network scanner dan port discovery
- **Masscan** - High-speed port scanner
- **Zmap** - Fast network scanner

### Web Application Testing
- **Gobuster** - Directory/file brute-forcer
- **Dirb** - Web content scanner
- **Nikto** - Web server vulnerability scanner
- **SQLMap** - SQL injection scanner
- **WPScan** - WordPress vulnerability scanner

### Password Security
- **Hydra** - Password cracker
- **John the Ripper** - Hash cracker
- **Hashcat** - Advanced password recovery

### Exploitation
- **Metasploit** - Exploitation framework
- **Ncrack** - Network authentication cracker

### System Enumeration
- **Enum4linux** - SMB/Windows enumeration
- **SMBClient** - SMB client tools
- **RPCClient** - RPC client tools

### Generic Commands
- **Custom Commands** - Eksekusi perintah sistem operasi apapun

## 🛠️ Instalasi

### Prasyarat
- Python 3.6 atau lebih baru
- Windows, Linux, atau macOS
- Akses ke mesin Kali Linux (untuk tools khusus)

### Instalasi Cepat

1. **Clone Repository**
```bash
git clone https://github.com/Wh0am123/MCP-Kali-Server.git
cd MCP-Kali-Server
```

2. **Jalankan Server**
```bash
# Windows
start_server.bat

# Linux/macOS
python simple_kali_server.py --port 5000
```

3. **Jalankan Client (Terminal Baru)**
```bash
# Windows
start_client.bat

# Linux/macOS
python simple_mcp_client.py --server http://localhost:5000 --interactive
```

### Instalasi Manual

1. **Install Dependencies (Opsional)**
```bash
python install.py
```

2. **Jalankan Server**
```bash
python simple_kali_server.py --port 5000 --debug
```

3. **Test Koneksi**
```bash
python test_connection.py
```

## 🚀 Penggunaan

### Mode Interaktif

Setelah menjalankan client, Anda dapat menggunakan perintah berikut:

```bash
Kali> health                    # Cek status server
Kali> nmap 192.168.1.1         # Network scanning
Kali> gobuster http://target.com # Directory scanning
Kali> dirb http://target.com    # Web content scanning
Kali> nikto http://target.com   # Web vulnerability scanning
Kali> exec whoami               # Execute custom command
Kali> help                      # Show help
Kali> quit                      # Exit
```

### API Endpoints

#### Health Check
```bash
curl http://localhost:5000/health
```

#### Execute Command
```bash
curl -X POST http://localhost:5000/api/command \
  -H "Content-Type: application/json" \
  -d '{"command": "whoami"}'
```

#### Nmap Scan
```bash
curl -X POST http://localhost:5000/api/tools/nmap \
  -H "Content-Type: application/json" \
  -d '{"target": "192.168.1.1", "scan_type": "-sV"}'
```

#### Gobuster Scan
```bash
curl -X POST http://localhost:5000/api/tools/gobuster \
  -H "Content-Type: application/json" \
  -d '{"url": "http://target.com", "mode": "dir"}'
```

### Konfigurasi Claude Desktop

Edit file konfigurasi di `C:\Users\USERNAME\AppData\Roaming\Claude\claude_desktop_config.json`:

```json
{
    "mcpServers": {
        "kali_mcp": {
            "command": "python3",
            "args": [
                "C:\\path\\to\\MCP-Kali-Server\\simple_mcp_client.py",
                "--server",
                "http://localhost:5000"
            ]
        }
    }
}
```

### Konfigurasi 5ire Desktop

Tambahkan MCP dengan command:
```bash
python3 C:\path\to\MCP-Kali-Server\simple_mcp_client.py http://localhost:5000
```

## 📊 Monitoring dan Logs

### Server Logs
Server menampilkan logs dengan format:
```
2024-01-01 12:00:00 [INFO] Starting Kali Linux Tools API Server on port 5000
2024-01-01 12:00:01 [INFO] Executing command: nmap -sV 192.168.1.1
2024-01-01 12:00:05 [INFO] Command completed successfully
```

### Health Monitoring
```bash
# Cek status server
curl http://localhost:5000/health

# Response example
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

## 🔧 Konfigurasi Lanjutan

### Mengubah Port Server
```bash
python simple_kali_server.py --port 8080
```

### Mengubah Server URL
```bash
python simple_mcp_client.py --server http://192.168.1.100:5000 --interactive
```

### Debug Mode
```bash
# Server debug mode
python simple_kali_server.py --debug --port 5000

# Client debug mode
python simple_mcp_client.py --debug --interactive
```

### Timeout Configuration
```bash
python simple_mcp_client.py --timeout 600 --interactive
```

## 🎯 Use Cases

### 1. Automated Penetration Testing
```python
# Contoh penggunaan dengan AI
client = SimpleKaliClient("http://localhost:5000")

# Network discovery
result = client.nmap_scan("192.168.1.0/24", "-sn")

# Web vulnerability scanning
result = client.nikto_scan("http://target.com")

# Directory enumeration
result = client.gobuster_scan("http://target.com", "dir")
```

### 2. CTF Challenge Solving
```python
# AI dapat menggunakan tools untuk menyelesaikan CTF
client.execute_command("curl -s http://ctf.example.com/challenge")
client.execute_command("gobuster dir -u http://ctf.example.com -w wordlist.txt")
```

### 3. Security Assessment
```python
# Comprehensive security assessment
tools = [
    ("nmap", "192.168.1.100"),
    ("nikto", "http://192.168.1.100"),
    ("gobuster", "http://192.168.1.100")
]

for tool, target in tools:
    result = client.execute_command(f"{tool} {target}")
    print(f"Tool: {tool}, Target: {target}, Result: {result}")
```

## ⚠️ Keamanan dan Etika

### ⚠️ Peringatan Penting
- **Hanya untuk tujuan edukasi dan testing yang sah**
- **Pastikan Anda memiliki izin sebelum melakukan scanning**
- **Jangan gunakan untuk aktivitas ilegal atau berbahaya**
- **Gunakan hanya di lingkungan yang terkontrol**

### 🔒 Best Practices
1. **Isolasi Jaringan**: Gunakan di jaringan terisolasi
2. **Firewall**: Konfigurasi firewall dengan benar
3. **Monitoring**: Monitor aktivitas dan logs
4. **Backup**: Backup data penting sebelum testing
5. **Documentation**: Dokumentasikan semua aktivitas

## 🐛 Troubleshooting

### Server tidak bisa start
```bash
# Cek port yang digunakan
netstat -an | findstr :5000

# Gunakan port lain
python simple_kali_server.py --port 8080
```

### Client tidak bisa connect
```bash
# Cek koneksi ke server
curl http://localhost:5000/health

# Cek firewall settings
# Windows: Windows Defender Firewall
# Linux: iptables atau ufw
```

### Tools tidak ditemukan
```bash
# Cek status tools
curl http://localhost:5000/health

# Install tools yang diperlukan
# Ubuntu/Debian: sudo apt install nmap gobuster dirb nikto
# Kali Linux: sudo apt update && sudo apt install kali-linux-full
```

### Performance Issues
```bash
# Kurangi timeout
python simple_mcp_client.py --timeout 60

# Gunakan debug mode untuk troubleshooting
python simple_kali_server.py --debug
```

## 📚 Dokumentasi Lengkap

- [Tools Description](TOOLS_DESCRIPTION.md) - Deskripsi lengkap semua tools
- [Installation Guide](README_INSTALL.md) - Panduan instalasi detail
- [API Reference](API_REFERENCE.md) - Dokumentasi API lengkap

## 🤝 Kontribusi

Kontribusi sangat diterima! Silakan:

1. Fork repository ini
2. Buat feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

## 📄 Lisensi

Distribusi di bawah Lisensi MIT. Lihat `LICENSE` untuk informasi lebih lanjut.

## 🙏 Acknowledgments

- [ProjectDiscovery](https://projectdiscovery.io/) untuk tools keamanan
- [Kali Linux](https://www.kali.org/) untuk platform testing
- [MCP Community](https://github.com/modelcontextprotocol) untuk protokol MCP

## 📞 Support

Jika mengalami masalah:

1. Cek [Troubleshooting](#-troubleshooting) section
2. Lihat [Issues](https://github.com/Wh0am123/MCP-Kali-Server/issues)
3. Buat issue baru dengan detail error
4. Join komunitas Discord

## 🔗 Links

- **GitHub**: https://github.com/Wh0am123/MCP-Kali-Server
- **Kali.org**: https://www.kali.org/tools/mcp-kali-server/
- **GitLab**: https://gitlab.com/kalilinux/packages/mcp-kali-server
- **Documentation**: https://docs.kali.org/tools/mcp-kali-server

---

**Happy Hacking! 🔥**

*MCP-Kali-Server - Bringing AI to Offensive Security*
