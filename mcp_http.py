"""HTTP entry point for the WebSim MCP server.

Runs the MCP Streamable HTTP transport on the host/port supplied by Render.
The official MCP SDK bundled in mcp 1.x reads these values from FastMCP
settings rather than accepting host/port as run() keyword arguments.
"""

import os

from src.server import mcp


if __name__ == "__main__":
    mcp.settings.host = os.getenv("HOST", "0.0.0.0")
    mcp.settings.port = int(os.getenv("PORT", "8000"))

    # Streamable HTTP is the current MCP HTTP transport.
    mcp.run(transport="streamable-http")
