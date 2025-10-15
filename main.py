#!/usr/bin/env python3
"""
Main entry point for MCP-Kali-Server Railway deployment
"""

import os
import sys

def main():
    """Main entry point"""
    # Import and run the server
    from simple_kali_server import run_server
    
    # Get port from environment (Railway sets PORT)
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("DEBUG_MODE", "0").lower() in ("1", "true", "yes", "y")
    
    print(f"Starting MCP-Kali-Server on port {port}")
    print(f"Debug mode: {debug}")
    
    # Run the server
    run_server(port=port, debug=debug)

if __name__ == "__main__":
    main()