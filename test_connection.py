#!/usr/bin/env python3
"""
Script untuk test koneksi MCP-Kali-Server
"""

import json
import sys
import time
from simple_mcp_client import SimpleKaliClient

def test_connection():
    """Test koneksi ke server"""
    print("=== Test Koneksi MCP-Kali-Server ===")
    
    # Initialize client
    client = SimpleKaliClient("http://localhost:5000")
    
    # Test 1: Health Check
    print("\n1. Testing Health Check...")
    health = client.check_health()
    if "error" in health:
        print(f"Health check gagal: {health['error']}")
        return False
    else:
        print(f"Health check berhasil: {health['status']}")
        print(f"   Tools status: {health.get('tools_status', {})}")
    
    # Test 2: Execute Simple Command
    print("\n2. Testing Command Execution...")
    result = client.execute_command("echo 'Hello from MCP-Kali-Server'")
    if "error" in result:
        print(f"Command execution gagal: {result['error']}")
        return False
    else:
        print(f"Command execution berhasil")
        print(f"   Output: {result.get('stdout', '').strip()}")
        print(f"   Return code: {result.get('return_code', 'N/A')}")
    
    # Test 3: Test System Info
    print("\n3. Testing System Info...")
    result = client.execute_command("whoami")
    if "error" not in result:
        print(f"System info berhasil")
        print(f"   User: {result.get('stdout', '').strip()}")
    else:
        print(f"System info gagal: {result['error']}")
    
    # Test 4: Test Directory Listing
    print("\n4. Testing Directory Listing...")
    result = client.execute_command("dir" if sys.platform == "win32" else "ls -la")
    if "error" not in result:
        print(f"Directory listing berhasil")
        print(f"   Output length: {len(result.get('stdout', ''))} characters")
    else:
        print(f"Directory listing gagal: {result['error']}")
    
    print("\n=== Test Selesai ===")
    print("Koneksi MCP-Kali-Server berhasil!")
    print("\nServer siap digunakan untuk:")
    print("- Network scanning (nmap)")
    print("- Web vulnerability scanning (nikto)")
    print("- Directory brute-forcing (gobuster, dirb)")
    print("- Custom command execution")
    
    return True

if __name__ == "__main__":
    try:
        test_connection()
    except KeyboardInterrupt:
        print("\nTest dihentikan oleh user")
    except Exception as e:
        print(f"\nError selama test: {str(e)}")
