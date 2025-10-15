#!/usr/bin/env python3
"""
Script untuk menginstall dependencies MCP-Kali-Server
"""

import subprocess
import sys
import os

def install_package(package):
    """Install package menggunakan pip"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"Berhasil menginstall {package}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Gagal menginstall {package}: {e}")
        return False

def main():
    """Main installation function"""
    print("Memulai instalasi MCP-Kali-Server...")
    
    # Daftar packages yang diperlukan
    packages = [
        "flask>=2.0.0",
        "requests>=2.25.0"
    ]
    
    # Coba install MCP package
    mcp_packages = [
        "mcp",
        "mcp-server-fastmcp"
    ]
    
    print("\nMenginstall dependencies utama...")
    success_count = 0
    for package in packages:
        if install_package(package):
            success_count += 1
    
    print("\nMenginstall MCP packages...")
    mcp_success = False
    for package in mcp_packages:
        if install_package(package):
            mcp_success = True
            break
    
    if not mcp_success:
        print("MCP package tidak ditemukan, akan menggunakan alternatif...")
        # Install fastmcp sebagai alternatif
        install_package("fastmcp")
    
    print(f"\nHasil instalasi:")
    print(f"   - Dependencies utama: {success_count}/{len(packages)} berhasil")
    print(f"   - MCP package: {'Berhasil' if mcp_success else 'Gagal'}")
    
    if success_count == len(packages):
        print("\nInstalasi berhasil! MCP-Kali-Server siap digunakan.")
        print("\nLangkah selanjutnya:")
        print("   1. Jalankan server: python kali_server.py")
        print("   2. Jalankan client: python mcp_server.py --server http://KALI_IP:5000")
    else:
        print("\nBeberapa package gagal diinstall. Silakan cek error di atas.")

if __name__ == "__main__":
    main()
