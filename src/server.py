"""Read-only WebSim MCP bridge."""

import os
from typing import Any

import httpx
from mcp.server.fastmcp import FastMCP

BASE_URL = os.getenv("WEBSIM_API_BASE", "https://api.websim.com").rstrip("/")
mcp = FastMCP("WebSim ChatGPT Server")

async def get_json(path: str, params: dict[str, Any] | None = None) -> Any:
    async with httpx.AsyncClient(timeout=20) as client:
        response = await client.get(f"{BASE_URL}{path}", params=params)
        response.raise_for_status()
        return response.json()

@mcp.tool()
async def websim_get_project(project_id: str) -> Any:
    """Get a WebSim project by ID."""
    return await get_json(f"/api/v1/projects/{project_id}")

@mcp.tool()
async def websim_get_project_by_slug(username: str, slug: str) -> Any:
    """Get a WebSim project by username and slug."""
    return await get_json(f"/api/v1/users/{username}/slugs/{slug}")

@mcp.tool()
async def websim_get_user(username_or_id: str) -> Any:
    """Get public WebSim user information."""
    return await get_json(f"/api/v1/users/{username_or_id}")

@mcp.tool()
async def websim_list_user_projects(username_or_id: str, limit: int = 20) -> Any:
    """List projects for a WebSim user."""
    limit = max(1, min(limit, 50))
    return await get_json(f"/api/v1/users/{username_or_id}/projects", {"first": limit})

@mcp.tool()
async def websim_list_public_projects(limit: int = 20, query: str | None = None) -> Any:
    """List public WebSim projects, optionally filtered by query."""
    limit = max(1, min(limit, 50))
    params: dict[str, Any] = {"first": limit}
    if query:
        params["query"] = query
    return await get_json("/api/v1/projects", params)

@mcp.tool()
async def websim_get_project_html(project_id: str, version: int) -> str:
    """Get raw HTML for a WebSim project revision."""
    async with httpx.AsyncClient(timeout=20) as client:
        response = await client.get(f"{BASE_URL}/api/v1/projects/{project_id}/revisions/{version}/html")
        response.raise_for_status()
        return response.text

@mcp.tool()
async def websim_trending_projects(limit: int = 12) -> Any:
    """Get trending WebSim projects."""
    limit = max(1, min(limit, 50))
    return await get_json("/api/v1/feed/trending", {"limit": limit, "offset": 0, "feed": "hot"})

if __name__ == "__main__":
    mcp.run()
