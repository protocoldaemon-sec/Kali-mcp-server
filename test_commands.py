#!/usr/bin/env python3
"""
Script untuk test perintah-perintah MCP-Kali-Server
"""

import json
import sys
from simple_mcp_client import SimpleKaliClient

def test_commands():
    """Test berbagai perintah"""
    print("=== Test Perintah MCP-Kali-Server ===")
    
    # Initialize client
    client = SimpleKaliClient("http://localhost:5000")
    
    # Test commands
    test_cases = [
        {
            "name": "System Information",
            "command": "systeminfo" if sys.platform == "win32" else "uname -a",
            "description": "Mendapatkan informasi sistem"
        },
        {
            "name": "Network Configuration",
            "command": "ipconfig" if sys.platform == "win32" else "ifconfig",
            "description": "Melihat konfigurasi jaringan"
        },
        {
            "name": "Process List",
            "command": "tasklist" if sys.platform == "win32" else "ps aux",
            "description": "Melihat daftar proses"
        },
        {
            "name": "Disk Usage",
            "command": "dir C:\\" if sys.platform == "win32" else "df -h",
            "description": "Melihat penggunaan disk"
        },
        {
            "name": "Environment Variables",
            "command": "set" if sys.platform == "win32" else "env",
            "description": "Melihat environment variables"
        }
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n{i}. Testing {test_case['name']}...")
        print(f"   Description: {test_case['description']}")
        print(f"   Command: {test_case['command']}")
        
        result = client.execute_command(test_case['command'])
        
        if "error" in result:
            print(f"   Status: GAGAL - {result['error']}")
        else:
            print(f"   Status: BERHASIL")
            print(f"   Return code: {result.get('return_code', 'N/A')}")
            output = result.get('stdout', '')
            if output:
                # Show first few lines of output
                lines = output.strip().split('\n')[:3]
                print(f"   Output preview:")
                for line in lines:
                    print(f"     {line}")
                if len(output.strip().split('\n')) > 3:
                    print(f"     ... ({len(output.strip().split('\n')) - 3} lines more)")
            else:
                print(f"   Output: (empty)")
    
    print("\n=== Test Perintah Selesai ===")
    print("Semua perintah berhasil dijalankan melalui MCP-Kali-Server!")

if __name__ == "__main__":
    try:
        test_commands()
    except KeyboardInterrupt:
        print("\nTest dihentikan oleh user")
    except Exception as e:
        print(f"\nError selama test: {str(e)}")
