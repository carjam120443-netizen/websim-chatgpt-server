"""HTTP entry point for the WebSim MCP server.

Uses the MCP SDK's ASGI Streamable HTTP application so Render can
serve it through uvicorn on the platform-provided port.
"""

import os

import uvicorn

from src.server import mcp


app = mcp.streamable_http_app()


if __name__ == "__main__":
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "8000"))
    uvicorn.run(app, host=host, port=port)
