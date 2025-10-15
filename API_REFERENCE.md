# API Reference - MCP-Kali-Server

## Base URL
```
http://localhost:5000
```

## Authentication
Tidak ada autentikasi yang diperlukan untuk penggunaan lokal.

## Response Format
Semua response menggunakan format JSON dengan struktur berikut:

### Success Response
```json
{
  "stdout": "command output",
  "stderr": "error output",
  "return_code": 0,
  "success": true,
  "timed_out": false,
  "partial_results": false
}
```

### Error Response
```json
{
  "error": "Error message",
  "success": false
}
```

## Endpoints

### 1. Health Check

#### GET /health
Mengecek status server dan ketersediaan tools.

**Response:**
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

**Example:**
```bash
curl http://localhost:5000/health
```

---

### 2. Generic Command Execution

#### POST /api/command
Menjalankan perintah sistem operasi apapun.

**Request Body:**
```json
{
  "command": "whoami"
}
```

**Response:**
```json
{
  "stdout": "desktop-590kglm\\lenovo",
  "stderr": "",
  "return_code": 0,
  "success": true,
  "timed_out": false,
  "partial_results": false
}
```

**Example:**
```bash
curl -X POST http://localhost:5000/api/command \
  -H "Content-Type: application/json" \
  -d '{"command": "whoami"}'
```

---

### 3. Nmap Scanner

#### POST /api/tools/nmap
Menjalankan scan jaringan menggunakan Nmap.

**Request Body:**
```json
{
  "target": "192.168.1.1",
  "scan_type": "-sV",
  "ports": "80,443,22",
  "additional_args": "-T4 -Pn"
}
```

**Parameters:**
- `target` (required): IP address atau hostname target
- `scan_type` (optional): Jenis scan (default: "-sV")
- `ports` (optional): Port yang akan di-scan
- `additional_args` (optional): Argumen tambahan

**Response:**
```json
{
  "stdout": "Starting Nmap 7.80...\nNmap scan report for 192.168.1.1...",
  "stderr": "",
  "return_code": 0,
  "success": true,
  "timed_out": false,
  "partial_results": false
}
```

**Example:**
```bash
curl -X POST http://localhost:5000/api/tools/nmap \
  -H "Content-Type: application/json" \
  -d '{
    "target": "192.168.1.1",
    "scan_type": "-sV",
    "ports": "80,443,22",
    "additional_args": "-T4 -Pn"
  }'
```

---

### 4. Gobuster Scanner

#### POST /api/tools/gobuster
Menjalankan directory/file brute-forcing menggunakan Gobuster.

**Request Body:**
```json
{
  "url": "http://target.com",
  "mode": "dir",
  "wordlist": "/usr/share/wordlists/dirb/common.txt",
  "additional_args": "-t 50"
}
```

**Parameters:**
- `url` (required): URL target
- `mode` (optional): Mode scan - "dir", "dns", "fuzz", "vhost" (default: "dir")
- `wordlist` (optional): Path ke wordlist file
- `additional_args` (optional): Argumen tambahan

**Response:**
```json
{
  "stdout": "Gobuster v3.0.1\n[+] Mode: dir\n[+] Url: http://target.com...",
  "stderr": "",
  "return_code": 0,
  "success": true,
  "timed_out": false,
  "partial_results": false
}
```

**Example:**
```bash
curl -X POST http://localhost:5000/api/tools/gobuster \
  -H "Content-Type: application/json" \
  -d '{
    "url": "http://target.com",
    "mode": "dir",
    "wordlist": "/usr/share/wordlists/dirb/common.txt"
  }'
```

---

### 5. Dirb Scanner

#### POST /api/tools/dirb
Menjalankan web content scanning menggunakan Dirb.

**Request Body:**
```json
{
  "url": "http://target.com",
  "wordlist": "/usr/share/wordlists/dirb/common.txt",
  "additional_args": "-r"
}
```

**Parameters:**
- `url` (required): URL target
- `wordlist` (optional): Path ke wordlist file
- `additional_args` (optional): Argumen tambahan

**Response:**
```json
{
  "stdout": "DIRB v2.22\n[+] Starting dirb...",
  "stderr": "",
  "return_code": 0,
  "success": true,
  "timed_out": false,
  "partial_results": false
}
```

**Example:**
```bash
curl -X POST http://localhost:5000/api/tools/dirb \
  -H "Content-Type: application/json" \
  -d '{
    "url": "http://target.com",
    "wordlist": "/usr/share/wordlists/dirb/common.txt"
  }'
```

---

### 6. Nikto Scanner

#### POST /api/tools/nikto
Menjalankan web server vulnerability scanning menggunakan Nikto.

**Request Body:**
```json
{
  "target": "http://target.com",
  "additional_args": "-output nikto_results.txt"
}
```

**Parameters:**
- `target` (required): URL atau IP target
- `additional_args` (optional): Argumen tambahan

**Response:**
```json
{
  "stdout": "- Nikto v2.1.6\n- Target IP: 192.168.1.100...",
  "stderr": "",
  "return_code": 0,
  "success": true,
  "timed_out": false,
  "partial_results": false
}
```

**Example:**
```bash
curl -X POST http://localhost:5000/api/tools/nikto \
  -H "Content-Type: application/json" \
  -d '{
    "target": "http://target.com",
    "additional_args": "-output nikto_results.txt"
  }'
```

---

### 7. SQLMap Scanner

#### POST /api/tools/sqlmap
Menjalankan SQL injection scanning menggunakan SQLMap.

**Request Body:**
```json
{
  "url": "http://target.com/page.php?id=1",
  "data": "user=admin&pass=admin",
  "additional_args": "--batch --dbs"
}
```

**Parameters:**
- `url` (required): URL target dengan parameter
- `data` (optional): POST data untuk testing
- `additional_args` (optional): Argumen tambahan

**Response:**
```json
{
  "stdout": "sqlmap/1.4.7#stable\n[!] legal disclaimer...",
  "stderr": "",
  "return_code": 0,
  "success": true,
  "timed_out": false,
  "partial_results": false
}
```

**Example:**
```bash
curl -X POST http://localhost:5000/api/tools/sqlmap \
  -H "Content-Type: application/json" \
  -d '{
    "url": "http://target.com/page.php?id=1",
    "additional_args": "--batch"
  }'
```

---

### 8. Metasploit Framework

#### POST /api/tools/metasploit
Menjalankan module Metasploit.

**Request Body:**
```json
{
  "module": "exploit/windows/smb/ms17_010_eternalblue",
  "options": {
    "RHOSTS": "192.168.1.100",
    "RPORT": "445",
    "LHOST": "192.168.1.50"
  }
}
```

**Parameters:**
- `module` (required): Path module Metasploit
- `options` (optional): Dictionary opsi module

**Response:**
```json
{
  "stdout": "msf6 > use exploit/windows/smb/ms17_010_eternalblue...",
  "stderr": "",
  "return_code": 0,
  "success": true,
  "timed_out": false,
  "partial_results": false
}
```

**Example:**
```bash
curl -X POST http://localhost:5000/api/tools/metasploit \
  -H "Content-Type: application/json" \
  -d '{
    "module": "exploit/windows/smb/ms17_010_eternalblue",
    "options": {
      "RHOSTS": "192.168.1.100"
    }
  }'
```

---

### 9. Hydra Password Cracker

#### POST /api/tools/hydra
Menjalankan password brute-forcing menggunakan Hydra.

**Request Body:**
```json
{
  "target": "192.168.1.100",
  "service": "ssh",
  "username": "admin",
  "password": "password123",
  "additional_args": "-t 4"
}
```

**Parameters:**
- `target` (required): IP atau hostname target
- `service` (required): Service yang akan di-attack
- `username` (optional): Username untuk testing
- `username_file` (optional): File berisi daftar username
- `password` (optional): Password untuk testing
- `password_file` (optional): File berisi daftar password
- `additional_args` (optional): Argumen tambahan

**Response:**
```json
{
  "stdout": "Hydra v9.0 (c) 2019 by van Hauser/THC...",
  "stderr": "",
  "return_code": 0,
  "success": true,
  "timed_out": false,
  "partial_results": false
}
```

**Example:**
```bash
curl -X POST http://localhost:5000/api/tools/hydra \
  -H "Content-Type: application/json" \
  -d '{
    "target": "192.168.1.100",
    "service": "ssh",
    "username": "admin",
    "password_file": "/usr/share/wordlists/rockyou.txt"
  }'
```

---

### 10. John the Ripper

#### POST /api/tools/john
Menjalankan hash cracking menggunakan John the Ripper.

**Request Body:**
```json
{
  "hash_file": "/path/to/hashes.txt",
  "wordlist": "/usr/share/wordlists/rockyou.txt",
  "format_type": "md5crypt",
  "additional_args": "--rules"
}
```

**Parameters:**
- `hash_file` (required): File berisi hash yang akan di-crack
- `wordlist` (optional): Wordlist untuk dictionary attack
- `format_type` (optional): Format hash
- `additional_args` (optional): Argumen tambahan

**Response:**
```json
{
  "stdout": "Using default input encoding: UTF-8\nLoaded 1 password hash...",
  "stderr": "",
  "return_code": 0,
  "success": true,
  "timed_out": false,
  "partial_results": false
}
```

**Example:**
```bash
curl -X POST http://localhost:5000/api/tools/john \
  -H "Content-Type: application/json" \
  -d '{
    "hash_file": "/path/to/hashes.txt",
    "wordlist": "/usr/share/wordlists/rockyou.txt"
  }'
```

---

### 11. WPScan

#### POST /api/tools/wpscan
Menjalankan WordPress vulnerability scanning menggunakan WPScan.

**Request Body:**
```json
{
  "url": "http://target.com",
  "additional_args": "--enumerate u,p"
}
```

**Parameters:**
- `url` (required): URL WordPress target
- `additional_args` (optional): Argumen tambahan

**Response:**
```json
{
  "stdout": "_______________________________________________________________\n         __          _______   _____...",
  "stderr": "",
  "return_code": 0,
  "success": true,
  "timed_out": false,
  "partial_results": false
}
```

**Example:**
```bash
curl -X POST http://localhost:5000/api/tools/wpscan \
  -H "Content-Type: application/json" \
  -d '{
    "url": "http://target.com",
    "additional_args": "--enumerate u"
  }'
```

---

### 12. Enum4linux

#### POST /api/tools/enum4linux
Menjalankan SMB/Windows enumeration menggunakan Enum4linux.

**Request Body:**
```json
{
  "target": "192.168.1.100",
  "additional_args": "-a"
}
```

**Parameters:**
- `target` (required): IP atau hostname target
- `additional_args` (optional): Argumen tambahan (default: "-a")

**Response:**
```json
{
  "stdout": "Starting enum4linux v0.8.9...",
  "stderr": "",
  "return_code": 0,
  "success": true,
  "timed_out": false,
  "partial_results": false
}
```

**Example:**
```bash
curl -X POST http://localhost:5000/api/tools/enum4linux \
  -H "Content-Type: application/json" \
  -d '{
    "target": "192.168.1.100",
    "additional_args": "-a"
  }'
```

---

## Error Codes

### HTTP Status Codes
- `200 OK` - Request berhasil
- `400 Bad Request` - Parameter tidak valid
- `404 Not Found` - Endpoint tidak ditemukan
- `500 Internal Server Error` - Error server

### Common Error Messages
- `"Command parameter is required"` - Parameter command kosong
- `"Target parameter is required"` - Parameter target kosong
- `"URL parameter is required"` - Parameter URL kosong
- `"Invalid mode: {mode}"` - Mode tidak valid
- `"Server error: {error}"` - Error server internal

## Rate Limiting
Tidak ada rate limiting yang diterapkan. Gunakan dengan bijak untuk menghindari overload server.

## Timeout
- Default timeout: 180 detik (3 menit)
- Dapat dikonfigurasi melalui parameter `--timeout`
- Command yang timeout akan dihentikan secara paksa

## Security Considerations
- Server berjalan di `0.0.0.0` (semua interface)
- Tidak ada autentikasi untuk penggunaan lokal
- Pastikan firewall dikonfigurasi dengan benar
- Hanya gunakan di jaringan yang aman
