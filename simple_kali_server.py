#!/usr/bin/env python3
"""
Simple Kali Server tanpa dependencies eksternal
Versi sederhana dari MCP-Kali-Server yang hanya menggunakan library standar Python
"""

import json
import logging
import os
import subprocess
import sys
import traceback
import threading
import time
from typing import Dict, Any
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

# Configuration
API_PORT = int(os.environ.get("PORT", os.environ.get("API_PORT", 5000)))
DEBUG_MODE = os.environ.get("DEBUG_MODE", "0").lower() in ("1", "true", "yes", "y")
COMMAND_TIMEOUT = 180  # 3 minutes default timeout

class CommandExecutor:
    """Class to handle command execution with better timeout management"""
    
    def __init__(self, command: str, timeout: int = COMMAND_TIMEOUT):
        self.command = command
        self.timeout = timeout
        self.process = None
        self.stdout_data = ""
        self.stderr_data = ""
        self.return_code = None
        self.timed_out = False
    
    def execute(self) -> Dict[str, Any]:
        """Execute the command and handle timeout gracefully"""
        logger.info(f"Executing command: {self.command}")
        
        try:
            self.process = subprocess.Popen(
                self.command,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1  # Line buffered
            )
            
            # Wait for the process to complete or timeout
            try:
                self.return_code = self.process.wait(timeout=self.timeout)
                self.stdout_data = self.process.stdout.read()
                self.stderr_data = self.process.stderr.read()
            except subprocess.TimeoutExpired:
                # Process timed out
                self.timed_out = True
                logger.warning(f"Command timed out after {self.timeout} seconds. Terminating process.")
                
                # Try to terminate gracefully first
                self.process.terminate()
                try:
                    self.process.wait(timeout=5)  # Give it 5 seconds to terminate
                except subprocess.TimeoutExpired:
                    # Force kill if it doesn't terminate
                    logger.warning("Process not responding to termination. Killing.")
                    self.process.kill()
                
                # Get partial output
                self.stdout_data = self.process.stdout.read()
                self.stderr_data = self.process.stderr.read()
                self.return_code = -1
            
            # Always consider it a success if we have output, even with timeout
            success = True if self.timed_out and (self.stdout_data or self.stderr_data) else (self.return_code == 0)
            
            return {
                "stdout": self.stdout_data,
                "stderr": self.stderr_data,
                "return_code": self.return_code,
                "success": success,
                "timed_out": self.timed_out,
                "partial_results": self.timed_out and (self.stdout_data or self.stderr_data)
            }
        
        except Exception as e:
            logger.error(f"Error executing command: {str(e)}")
            logger.error(traceback.format_exc())
            return {
                "stdout": self.stdout_data,
                "stderr": f"Error executing command: {str(e)}\n{self.stderr_data}",
                "return_code": -1,
                "success": False,
                "timed_out": False,
                "partial_results": bool(self.stdout_data or self.stderr_data)
            }

def execute_command(command: str) -> Dict[str, Any]:
    """
    Execute a shell command and return the result
    
    Args:
        command: The command to execute
        
    Returns:
        A dictionary containing the stdout, stderr, and return code
    """
    executor = CommandExecutor(command)
    return executor.execute()

class KaliAPIHandler(BaseHTTPRequestHandler):
    """HTTP Request Handler for Kali API Server"""
    
    def do_GET(self):
        """Handle GET requests"""
        if self.path == "/health":
            self.handle_health_check()
        else:
            self.send_error(404, "Not Found")
    
    def do_POST(self):
        """Handle POST requests"""
        if self.path == "/api/command":
            self.handle_generic_command()
        elif self.path.startswith("/api/tools/"):
            self.handle_tool_command()
        else:
            self.send_error(404, "Not Found")
    
    def handle_health_check(self):
        """Handle health check endpoint"""
        # Check if essential tools are installed
        essential_tools = ["nmap", "gobuster", "dirb", "nikto"]
        tools_status = {}
        
        for tool in essential_tools:
            try:
                result = execute_command(f"which {tool}")
                tools_status[tool] = result["success"]
            except:
                tools_status[tool] = False
        
        all_essential_tools_available = all(tools_status.values())
        
        response = {
            "status": "healthy",
            "message": "Kali Linux Tools API Server is running",
            "tools_status": tools_status,
            "all_essential_tools_available": all_essential_tools_available
        }
        
        self.send_json_response(response)
    
    def handle_generic_command(self):
        """Handle generic command execution"""
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            params = json.loads(post_data.decode('utf-8'))
            command = params.get("command", "")
            
            if not command:
                logger.warning("Command endpoint called without command parameter")
                self.send_error(400, "Command parameter is required")
                return
            
            result = execute_command(command)
            self.send_json_response(result)
        except Exception as e:
            logger.error(f"Error in command endpoint: {str(e)}")
            logger.error(traceback.format_exc())
            self.send_error(500, f"Server error: {str(e)}")
    
    def handle_tool_command(self):
        """Handle tool-specific commands"""
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            params = json.loads(post_data.decode('utf-8'))
            
            # Extract tool name from path
            tool_name = self.path.split("/")[-1]
            
            if tool_name == "nmap":
                self.handle_nmap(params)
            elif tool_name == "gobuster":
                self.handle_gobuster(params)
            elif tool_name == "dirb":
                self.handle_dirb(params)
            elif tool_name == "nikto":
                self.handle_nikto(params)
            else:
                self.send_error(404, f"Tool {tool_name} not supported")
        except Exception as e:
            logger.error(f"Error in tool endpoint: {str(e)}")
            logger.error(traceback.format_exc())
            self.send_error(500, f"Server error: {str(e)}")
    
    def handle_nmap(self, params):
        """Handle nmap command"""
        target = params.get("target", "")
        scan_type = params.get("scan_type", "-sV")
        ports = params.get("ports", "")
        additional_args = params.get("additional_args", "-T4 -Pn")
        
        if not target:
            self.send_error(400, "Target parameter is required")
            return
        
        command = f"nmap {scan_type}"
        
        if ports:
            command += f" -p {ports}"
        
        if additional_args:
            command += f" {additional_args}"
        
        command += f" {target}"
        
        result = execute_command(command)
        self.send_json_response(result)
    
    def handle_gobuster(self, params):
        """Handle gobuster command"""
        url = params.get("url", "")
        mode = params.get("mode", "dir")
        wordlist = params.get("wordlist", "/usr/share/wordlists/dirb/common.txt")
        additional_args = params.get("additional_args", "")
        
        if not url:
            self.send_error(400, "URL parameter is required")
            return
        
        if mode not in ["dir", "dns", "fuzz", "vhost"]:
            self.send_error(400, f"Invalid mode: {mode}. Must be one of: dir, dns, fuzz, vhost")
            return
        
        command = f"gobuster {mode} -u {url} -w {wordlist}"
        
        if additional_args:
            command += f" {additional_args}"
        
        result = execute_command(command)
        self.send_json_response(result)
    
    def handle_dirb(self, params):
        """Handle dirb command"""
        url = params.get("url", "")
        wordlist = params.get("wordlist", "/usr/share/wordlists/dirb/common.txt")
        additional_args = params.get("additional_args", "")
        
        if not url:
            self.send_error(400, "URL parameter is required")
            return
        
        command = f"dirb {url} {wordlist}"
        
        if additional_args:
            command += f" {additional_args}"
        
        result = execute_command(command)
        self.send_json_response(result)
    
    def handle_nikto(self, params):
        """Handle nikto command"""
        target = params.get("target", "")
        additional_args = params.get("additional_args", "")
        
        if not target:
            self.send_error(400, "Target parameter is required")
            return
        
        command = f"nikto -h {target}"
        
        if additional_args:
            command += f" {additional_args}"
        
        result = execute_command(command)
        self.send_json_response(result)
    
    def send_json_response(self, data):
        """Send JSON response"""
        response = json.dumps(data, indent=2)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        self.wfile.write(response.encode('utf-8'))
    
    def log_message(self, format, *args):
        """Override log_message to use our logger"""
        logger.info(f"{self.address_string()} - {format % args}")

def run_server(port=API_PORT, debug=DEBUG_MODE):
    """Run the Kali API Server"""
    server_address = ('0.0.0.0', port)
    httpd = HTTPServer(server_address, KaliAPIHandler)
    
    logger.info(f"Starting Kali Linux Tools API Server on port {port}")
    logger.info(f"Debug mode: {debug}")
    logger.info(f"Server running at http://0.0.0.0:{port}")
    logger.info("Available endpoints:")
    logger.info("  GET  /health - Health check")
    logger.info("  POST /api/command - Execute generic command")
    logger.info("  POST /api/tools/nmap - Execute nmap scan")
    logger.info("  POST /api/tools/gobuster - Execute gobuster scan")
    logger.info("  POST /api/tools/dirb - Execute dirb scan")
    logger.info("  POST /api/tools/nikto - Execute nikto scan")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        logger.info("Server stopped by user")
        httpd.shutdown()

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Run the Kali Linux API Server")
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")
    parser.add_argument("--port", type=int, default=API_PORT, help=f"Port for the API server (default: {API_PORT})")
    
    args = parser.parse_args()
    
    # Set configuration from command line arguments
    if args.debug:
        DEBUG_MODE = True
        logging.getLogger().setLevel(logging.DEBUG)
    
    if args.port != API_PORT:
        API_PORT = args.port
    
    run_server(API_PORT, DEBUG_MODE)
