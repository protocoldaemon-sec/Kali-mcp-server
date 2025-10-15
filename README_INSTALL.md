# MCP-Kali-Server - Panduan Instalasi

## 🚀 Instalasi Cepat

### Prasyarat
- Python 3.6 atau lebih baru
- Windows, Linux, atau macOS

### Langkah 1: Clone Repository
```bash
git clone https://github.com/Wh0am123/MCP-Kali-Server.git
cd MCP-Kali-Server
```

### Langkah 2: Jalankan Server
```bash
# Windows
start_server.bat

# Linux/macOS
python simple_kali_server.py --port 5000
```

### Langkah 3: Jalankan Client (Terminal Baru)
```bash
# Windows
start_client.bat

# Linux/macOS
python simple_mcp_client.py --server http://localhost:5000 --interactive
```

## 📋 Fitur yang Tersedia

### Tools yang Didukung
- **nmap** - Network scanning
- **gobuster** - Directory/file brute-forcing
- **dirb** - Web content scanner
- **nikto** - Web server scanner
- **exec** - Execute arbitrary commands

### Mode Interaktif
Setelah menjalankan client, Anda dapat menggunakan perintah berikut:

```
Kali> health                    # Cek status server
Kali> nmap 192.168.1.1         # Scan network
Kali> gobuster http://target.com # Directory scanning
Kali> dirb http://target.com    # Web content scanning
Kali> nikto http://target.com   # Web vulnerability scanning
Kali> exec whoami               # Execute command
Kali> help                      # Show help
Kali> quit                      # Exit
```

## 🔧 Konfigurasi

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
python simple_kali_server.py --debug --port 5000
python simple_mcp_client.py --debug --interactive
```

## 🌐 API Endpoints

Server menyediakan REST API endpoints:

- `GET /health` - Health check
- `POST /api/command` - Execute generic command
- `POST /api/tools/nmap` - Execute nmap scan
- `POST /api/tools/gobuster` - Execute gobuster scan
- `POST /api/tools/dirb` - Execute dirb scan
- `POST /api/tools/nikto` - Execute nikto scan

### Contoh API Usage
```bash
# Health check
curl http://localhost:5000/health

# Execute command
curl -X POST http://localhost:5000/api/command \
  -H "Content-Type: application/json" \
  -d '{"command": "whoami"}'

# Nmap scan
curl -X POST http://localhost:5000/api/tools/nmap \
  -H "Content-Type: application/json" \
  -d '{"target": "192.168.1.1", "scan_type": "-sV"}'
```

## ⚠️ Keamanan

- Server berjalan di `0.0.0.0` (semua interface)
- Pastikan firewall dikonfigurasi dengan benar
- Hanya gunakan di jaringan yang aman
- Jangan expose ke internet tanpa autentikasi

## 🐛 Troubleshooting

### Server tidak bisa start
- Pastikan port 5000 tidak digunakan aplikasi lain
- Coba gunakan port lain: `--port 8080`

### Client tidak bisa connect
- Pastikan server sudah berjalan
- Cek URL server: `--server http://localhost:5000`
- Cek firewall settings

### Tools tidak ditemukan
- Pastikan tools (nmap, gobuster, dll) sudah terinstall
- Cek PATH environment variable
- Gunakan `health` command untuk cek status tools

## 📝 Logs

Server dan client akan menampilkan logs dengan format:
```
2024-01-01 12:00:00 [INFO] Starting Kali Linux Tools API Server on port 5000
2024-01-01 12:00:01 [INFO] Executing command: nmap -sV 192.168.1.1
```

## 🔄 Update

Untuk update ke versi terbaru:
```bash
git pull origin main
```

## 📞 Support

Jika mengalami masalah:
1. Cek logs untuk error messages
2. Pastikan semua prasyarat terpenuhi
3. Coba restart server dan client
4. Buat issue di GitHub repository
