"""HTTP entry point for the WebSim MCP server.

The MCP SDK's Streamable HTTP transport exposes the server at /mcp.
"""

from src.server import mcp


if __name__ == "__main__":
    # Streamable HTTP is the current MCP HTTP transport.
    # JSON responses are enabled for simpler HTTP clients and deployment.
    mcp.run(transport="streamable-http")
