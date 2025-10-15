#!/usr/bin/env python3
"""
Simple MCP Client untuk MCP-Kali-Server
Versi sederhana yang tidak memerlukan dependencies eksternal
"""

import json
import logging
import sys
import argparse
import urllib.request
import urllib.parse
import urllib.error
from typing import Dict, Any, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

# Default configuration
DEFAULT_KALI_SERVER = "http://localhost:5000"
DEFAULT_REQUEST_TIMEOUT = 300  # 5 minutes default timeout for API requests

class SimpleKaliClient:
    """Simple client for communicating with the Kali Linux Tools API Server"""
    
    def __init__(self, server_url: str, timeout: int = DEFAULT_REQUEST_TIMEOUT):
        """
        Initialize the Kali Tools Client
        
        Args:
            server_url: URL of the Kali Tools API Server
            timeout: Request timeout in seconds
        """
        self.server_url = server_url.rstrip("/")
        self.timeout = timeout
        logger.info(f"Initialized Kali Tools Client connecting to {server_url}")
        
    def safe_get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Perform a GET request with optional query parameters.
        
        Args:
            endpoint: API endpoint path (without leading slash)
            params: Optional query parameters
            
        Returns:
            Response data as dictionary
        """
        if params is None:
            params = {}

        url = f"{self.server_url}/{endpoint}"
        
        if params:
            query_string = urllib.parse.urlencode(params)
            url += f"?{query_string}"

        try:
            logger.debug(f"GET {url}")
            request = urllib.request.Request(url)
            request.add_header('User-Agent', 'SimpleKaliClient/1.0')
            
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                data = response.read().decode('utf-8')
                return json.loads(data)
        except urllib.error.URLError as e:
            logger.error(f"Request failed: {str(e)}")
            return {"error": f"Request failed: {str(e)}", "success": False}
        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")
            return {"error": f"Unexpected error: {str(e)}", "success": False}

    def safe_post(self, endpoint: str, json_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Perform a POST request with JSON data.
        
        Args:
            endpoint: API endpoint path (without leading slash)
            json_data: JSON data to send
            
        Returns:
            Response data as dictionary
        """
        url = f"{self.server_url}/{endpoint}"
        
        try:
            logger.debug(f"POST {url} with data: {json_data}")
            data = json.dumps(json_data).encode('utf-8')
            
            request = urllib.request.Request(url, data=data)
            request.add_header('Content-Type', 'application/json')
            request.add_header('User-Agent', 'SimpleKaliClient/1.0')
            
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                response_data = response.read().decode('utf-8')
                return json.loads(response_data)
        except urllib.error.URLError as e:
            logger.error(f"Request failed: {str(e)}")
            return {"error": f"Request failed: {str(e)}", "success": False}
        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")
            return {"error": f"Unexpected error: {str(e)}", "success": False}

    def execute_command(self, command: str) -> Dict[str, Any]:
        """
        Execute a generic command on the Kali server
        
        Args:
            command: Command to execute
            
        Returns:
            Command execution results
        """
        return self.safe_post("api/command", {"command": command})
    
    def check_health(self) -> Dict[str, Any]:
        """
        Check the health of the Kali Tools API Server
        
        Returns:
            Health status information
        """
        return self.safe_get("health")

    def nmap_scan(self, target: str, scan_type: str = "-sV", ports: str = "", additional_args: str = "") -> Dict[str, Any]:
        """
        Execute an Nmap scan against a target.
        
        Args:
            target: The IP address or hostname to scan
            scan_type: Scan type (e.g., -sV for version detection)
            ports: Comma-separated list of ports or port ranges
            additional_args: Additional Nmap arguments
            
        Returns:
            Scan results
        """
        data = {
            "target": target,
            "scan_type": scan_type,
            "ports": ports,
            "additional_args": additional_args
        }
        return self.safe_post("api/tools/nmap", data)

    def gobuster_scan(self, url: str, mode: str = "dir", wordlist: str = "/usr/share/wordlists/dirb/common.txt", additional_args: str = "") -> Dict[str, Any]:
        """
        Execute Gobuster to find directories, DNS subdomains, or virtual hosts.
        
        Args:
            url: The target URL
            mode: Scan mode (dir, dns, fuzz, vhost)
            wordlist: Path to wordlist file
            additional_args: Additional Gobuster arguments
            
        Returns:
            Scan results
        """
        data = {
            "url": url,
            "mode": mode,
            "wordlist": wordlist,
            "additional_args": additional_args
        }
        return self.safe_post("api/tools/gobuster", data)

    def dirb_scan(self, url: str, wordlist: str = "/usr/share/wordlists/dirb/common.txt", additional_args: str = "") -> Dict[str, Any]:
        """
        Execute Dirb web content scanner.
        
        Args:
            url: The target URL
            wordlist: Path to wordlist file
            additional_args: Additional Dirb arguments
            
        Returns:
            Scan results
        """
        data = {
            "url": url,
            "wordlist": wordlist,
            "additional_args": additional_args
        }
        return self.safe_post("api/tools/dirb", data)

    def nikto_scan(self, target: str, additional_args: str = "") -> Dict[str, Any]:
        """
        Execute Nikto web server scanner.
        
        Args:
            target: The target URL or IP
            additional_args: Additional Nikto arguments
            
        Returns:
            Scan results
        """
        data = {
            "target": target,
            "additional_args": additional_args
        }
        return self.safe_post("api/tools/nikto", data)

def interactive_mode(client: SimpleKaliClient):
    """Run interactive mode for testing"""
    print("\n=== MCP-Kali-Server Interactive Mode ===")
    print("Ketik 'help' untuk melihat perintah yang tersedia")
    print("Ketik 'quit' untuk keluar")
    
    while True:
        try:
            command = input("\nKali> ").strip()
            
            if command.lower() in ['quit', 'exit', 'q']:
                print("Keluar dari interactive mode...")
                break
            elif command.lower() == 'help':
                print_help()
            elif command.lower() == 'health':
                result = client.check_health()
                print(json.dumps(result, indent=2))
            elif command.startswith('nmap '):
                # Parse nmap command
                parts = command.split()
                if len(parts) < 2:
                    print("Usage: nmap <target> [scan_type] [ports] [additional_args]")
                    continue
                target = parts[1]
                scan_type = parts[2] if len(parts) > 2 else "-sV"
                ports = parts[3] if len(parts) > 3 else ""
                additional_args = " ".join(parts[4:]) if len(parts) > 4 else ""
                
                print(f"Menjalankan nmap scan pada {target}...")
                result = client.nmap_scan(target, scan_type, ports, additional_args)
                print("Hasil nmap:")
                print(result.get('stdout', ''))
                if result.get('stderr'):
                    print("Error:")
                    print(result.get('stderr', ''))
            elif command.startswith('gobuster '):
                # Parse gobuster command
                parts = command.split()
                if len(parts) < 2:
                    print("Usage: gobuster <url> [mode] [wordlist] [additional_args]")
                    continue
                url = parts[1]
                mode = parts[2] if len(parts) > 2 else "dir"
                wordlist = parts[3] if len(parts) > 3 else "/usr/share/wordlists/dirb/common.txt"
                additional_args = " ".join(parts[4:]) if len(parts) > 4 else ""
                
                print(f"Menjalankan gobuster scan pada {url}...")
                result = client.gobuster_scan(url, mode, wordlist, additional_args)
                print("Hasil gobuster:")
                print(result.get('stdout', ''))
                if result.get('stderr'):
                    print("Error:")
                    print(result.get('stderr', ''))
            elif command.startswith('dirb '):
                # Parse dirb command
                parts = command.split()
                if len(parts) < 2:
                    print("Usage: dirb <url> [wordlist] [additional_args]")
                    continue
                url = parts[1]
                wordlist = parts[2] if len(parts) > 2 else "/usr/share/wordlists/dirb/common.txt"
                additional_args = " ".join(parts[3:]) if len(parts) > 3 else ""
                
                print(f"Menjalankan dirb scan pada {url}...")
                result = client.dirb_scan(url, wordlist, additional_args)
                print("Hasil dirb:")
                print(result.get('stdout', ''))
                if result.get('stderr'):
                    print("Error:")
                    print(result.get('stderr', ''))
            elif command.startswith('nikto '):
                # Parse nikto command
                parts = command.split()
                if len(parts) < 2:
                    print("Usage: nikto <target> [additional_args]")
                    continue
                target = parts[1]
                additional_args = " ".join(parts[2:]) if len(parts) > 2 else ""
                
                print(f"Menjalankan nikto scan pada {target}...")
                result = client.nikto_scan(target, additional_args)
                print("Hasil nikto:")
                print(result.get('stdout', ''))
                if result.get('stderr'):
                    print("Error:")
                    print(result.get('stderr', ''))
            elif command.startswith('exec '):
                # Execute generic command
                cmd = command[5:]  # Remove 'exec ' prefix
                if not cmd:
                    print("Usage: exec <command>")
                    continue
                
                print(f"Menjalankan perintah: {cmd}")
                result = client.execute_command(cmd)
                print("Hasil:")
                print(result.get('stdout', ''))
                if result.get('stderr'):
                    print("Error:")
                    print(result.get('stderr', ''))
            else:
                print("Perintah tidak dikenali. Ketik 'help' untuk melihat perintah yang tersedia.")
                
        except KeyboardInterrupt:
            print("\nKeluar dari interactive mode...")
            break
        except Exception as e:
            print(f"Error: {str(e)}")

def print_help():
    """Print help information"""
    print("\nPerintah yang tersedia:")
    print("  health                    - Cek status server")
    print("  nmap <target> [options]   - Jalankan nmap scan")
    print("  gobuster <url> [options]  - Jalankan gobuster scan")
    print("  dirb <url> [options]      - Jalankan dirb scan")
    print("  nikto <target> [options]  - Jalankan nikto scan")
    print("  exec <command>            - Jalankan perintah umum")
    print("  help                      - Tampilkan bantuan ini")
    print("  quit                      - Keluar dari program")

def main():
    """Main entry point for the MCP client."""
    parser = argparse.ArgumentParser(description="Simple MCP Client for Kali Tools")
    parser.add_argument("--server", type=str, default=DEFAULT_KALI_SERVER, 
                      help=f"Kali API server URL (default: {DEFAULT_KALI_SERVER})")
    parser.add_argument("--timeout", type=int, default=DEFAULT_REQUEST_TIMEOUT,
                      help=f"Request timeout in seconds (default: {DEFAULT_REQUEST_TIMEOUT})")
    parser.add_argument("--debug", action="store_true", help="Enable debug logging")
    parser.add_argument("--interactive", action="store_true", help="Run in interactive mode")
    
    args = parser.parse_args()
    
    # Configure logging based on debug flag
    if args.debug:
        logger.setLevel(logging.DEBUG)
        logger.debug("Debug logging enabled")
    
    # Initialize the Kali Tools client
    client = SimpleKaliClient(args.server, args.timeout)
    
    # Check server health and log the result
    health = client.check_health()
    if "error" in health:
        logger.warning(f"Tidak dapat terhubung ke Kali API server di {args.server}: {health['error']}")
        logger.warning("Client akan tetap berjalan, tetapi eksekusi tool mungkin gagal")
    else:
        logger.info(f"Berhasil terhubung ke Kali API server di {args.server}")
        logger.info(f"Status server: {health['status']}")
        if not health.get("all_essential_tools_available", False):
            logger.warning("Tidak semua tool penting tersedia di Kali server")
            missing_tools = [tool for tool, available in health.get("tools_status", {}).items() if not available]
            if missing_tools:
                logger.warning(f"Tool yang hilang: {', '.join(missing_tools)}")
    
    if args.interactive:
        interactive_mode(client)
    else:
        print("MCP-Kali-Server Client siap digunakan!")
        print("Gunakan --interactive untuk mode interaktif")
        print("Gunakan --help untuk melihat opsi lainnya")

if __name__ == "__main__":
    main()
