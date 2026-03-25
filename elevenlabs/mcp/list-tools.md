# List MCP Server Tools API Documentation

## Overview

The ElevenLabs API provides an endpoint to retrieve all available tools for a specific MCP server configuration.

## Endpoint Details

**Method:** GET
**URL:** `https://api.elevenlabs.io/v1/convai/mcp-servers/{mcp_server_id}/tools`

## Purpose

This endpoint allows you to "retrieve all tools available for a specific MCP server configuration."

## Required Parameters

- **mcp_server_id** (path parameter): The identifier for the MCP Server you want to query

## Optional Parameters

- **xi-api-key** (header): Your ElevenLabs API authentication key

## Response Structure

The API returns a `ListMcpToolsResponseModel` containing:
- **success** (boolean): Operation status indicator
- **tools** (array): List of available Tool objects, each including:
  - name and inputSchema (required fields)
  - title, description, outputSchema (optional)
  - annotations with hints about tool behavior
- **error_message** (string): Details if the operation fails

## Important Note About Tool Annotations

The documentation emphasizes that "all properties in ToolAnnotations are **hints**. They are not guaranteed to provide a faithful description of tool behavior."

## HTTP Response Codes

- **200:** Successful response with tool list
- **422:** Validation error in request parameters
