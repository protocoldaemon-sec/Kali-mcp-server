#!/usr/bin/env python3
"""
Alternative entry point for MCP-Kali-Server
Railway will automatically run this file if main.py is not found
"""

import os
import sys
from simple_kali_server import run_server

def create_app():
    """Create and return the Flask app"""
    from simple_kali_server import app
    return app

if __name__ == "__main__":
    # Set default port for Railway
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("DEBUG_MODE", "0").lower() in ("1", "true", "yes", "y")
    
    print(f"Starting MCP-Kali-Server on port {port}")
    run_server(port=port, debug=debug)
