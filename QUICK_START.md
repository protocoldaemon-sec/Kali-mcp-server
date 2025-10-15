# Quick Start Guide - MCP-Kali-Server

## 🚀 Mulai dalam 5 Menit

### Langkah 1: Download dan Setup
```bash
# Clone repository
git clone https://github.com/Wh0am123/MCP-Kali-Server.git
cd MCP-Kali-Server

# Atau download ZIP dan extract
```

### Langkah 2: Jalankan Server
```bash
# Windows
start_server.bat

# Linux/macOS
python simple_kali_server.py --port 5000
```

### Langkah 3: Test Koneksi
```bash
# Buka terminal baru
cd MCP-Kali-Server
python test_connection.py
```

### Langkah 4: Mulai Menggunakan
```bash
# Mode interaktif
python simple_mcp_client.py --server http://localhost:5000 --interactive

# Atau gunakan API langsung
curl http://localhost:5000/health
```

## 🎯 Contoh Penggunaan Cepat

### 1. Cek Status Server
```bash
curl http://localhost:5000/health
```

### 2. Jalankan Perintah Sistem
```bash
curl -X POST http://localhost:5000/api/command \
  -H "Content-Type: application/json" \
  -d '{"command": "whoami"}'
```

### 3. Network Scanning (jika nmap tersedia)
```bash
curl -X POST http://localhost:5000/api/tools/nmap \
  -H "Content-Type: application/json" \
  -d '{"target": "127.0.0.1", "scan_type": "-sn"}'
```

### 4. Web Scanning (jika gobuster tersedia)
```bash
curl -X POST http://localhost:5000/api/tools/gobuster \
  -H "Content-Type: application/json" \
  -d '{"url": "http://httpbin.org", "mode": "dir"}'
```

## 🔧 Konfigurasi Cepat

### Claude Desktop
Edit `C:\Users\USERNAME\AppData\Roaming\Claude\claude_desktop_config.json`:
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

### 5ire Desktop
Tambahkan MCP dengan command:
```bash
python3 C:\path\to\MCP-Kali-Server\simple_mcp_client.py http://localhost:5000
```

## 🐛 Troubleshooting Cepat

### Server tidak start
```bash
# Cek port
netstat -an | findstr :5000

# Gunakan port lain
python simple_kali_server.py --port 8080
```

### Client tidak connect
```bash
# Test koneksi
curl http://localhost:5000/health

# Cek firewall
```

### Tools tidak ditemukan
```bash
# Cek status tools
curl http://localhost:5000/health

# Install tools (Ubuntu/Debian)
sudo apt install nmap gobuster dirb nikto
```

## 📚 Next Steps

1. **Baca Dokumentasi Lengkap**: [README.md](README.md)
2. **Pelajari API**: [API_REFERENCE.md](API_REFERENCE.md)
3. **Lihat Tools**: [TOOLS_DESCRIPTION.md](TOOLS_DESCRIPTION.md)
4. **Install Guide**: [README_INSTALL.md](README_INSTALL.md)

## 🎉 Selamat!

MCP-Kali-Server siap digunakan! Mulai eksplorasi dengan AI-powered penetration testing.
