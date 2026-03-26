# Sync MCP Server Capabilities

`POST /accounts/{account_id}/access/ai-controls/mcp/servers/{id}/sync`

Syncs an MCP server's tool catalog with the portal.

## Parameters

- **id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200



- **result** (object): 
- **success** (boolean): 

### 404

Not Found

- **errors** (array): 
- **success** (boolean):
