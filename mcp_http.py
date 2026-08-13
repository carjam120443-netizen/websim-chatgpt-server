"""HTTP entry point for the WebSim MCP server.

Runs the MCP Streamable HTTP transport on the host/port supplied by Render.
"""

import os

from src.server import mcp


if __name__ == "__main__":
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "8000"))

    # Streamable HTTP is the current MCP HTTP transport.
    # Render requires the service to bind to 0.0.0.0 and its assigned PORT.
    mcp.run(
        transport="streamable-http",
        host=host,
        port=port,
    )
