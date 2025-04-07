# MCP Kali Server

**Kali MCP Server** is a lightweight API bridge that connects MCP Clients (e.g: Claude Desktop, [5ire](https://github.com/nanbingxyz/5ire)) to the API server which allows excuting commands on a Linux terminal.

This allows the MCP to run terminal commands like `nmap`, `nxc` or any other tool, interact with web applications using tools like `curl`, `wget`, `gobuster`. 
 And perform **AI-assisted penetration testing**, solving **CTF web challenge** in real time, helping in **solving machines from HTB or THM**.

---

## 🔍 Use Case

The goal is to enable AI-driven offensive security testing by:

- Letting the MCP interact with AI endpoints like OpenAI, Claude, DeepSeek, or any other models.
- Exposing an API to execute commands on a Kali machine.
- Using AI to suggest and run terminal commands to solve CTF challenges or automate recon/exploitation tasks.
- Allowing MCP apps to send custom requests (e.g., `curl`, `nmap`, `ffuf`, etc.) and receive structured outputs.

---

## 🚀 Features

- 🧠 **AI Endpoint Integration**: Connect your kali to any MCP of your liking such as claude desktop or 5ier.
- 🖥️ **Command Execution API**: Exposes a controlled API to execute terminal commands on your Kali Linux machine.
- 🕸️ **Web Challenge Support**: AI can interact with APIs, capture flags, or brute-force login forms via `curl` and `hydra`.
- 🔐 **Designed for Offensive Security Professionals**: Ideal for red teamers, bug bounty hunters, or CTF players automating common tasks.

---

## 🛠️ Installation

### On your Linux Machine (Will act as MCP Server)
```bash
git clone https://github.com/Wh0am123/MCP-Kali-Server.git
cd MCP-Kali-Server
python3 kali_server.py
```

### On your MCP Client (You can run on Windows or Linux)
- You will want to run `python3 /absolute/path/to/mcp_server.py http://LINUX_IP:5000`

#### Configuration for claude desktop:
edit (C:\Users\USERNAME\AppData\Roaming\Claude\claude_desktop_config.json)

```json
{
    "mcpServers": {
        "kali_mcp": {
            "command": "python3",
            "args": [
                "/absolute/path/to/mcp_server.py",
                "http://LINUX_IP:5000/"
            ]
        }
    }
}
```

#### Configuration for [5ire](https://github.com/nanbingxyz/5ire) Desktop Application:
- Simply add an MCP with the command `python3 /absolute/path/to/mcp_server.py http://LINUX_IP:5000` and it will automatically generate the needed configuration files.
