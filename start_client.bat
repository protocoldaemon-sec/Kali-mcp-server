@echo off
echo Starting MCP-Kali-Server Client...
echo.
echo Client akan terhubung ke http://localhost:5000
echo.
python simple_mcp_client.py --server http://localhost:5000 --interactive
pause
