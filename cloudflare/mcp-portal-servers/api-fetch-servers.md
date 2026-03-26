# Read the details of a MCP Server

`GET /accounts/{account_id}/access/ai-controls/mcp/servers/{id}`

Retrieves gateway configuration for MCP portals.

## Parameters

- **account_id** (string, required) [path]: 
- **id** (string, required) [path]: 

## Response

### 200

Returns a single object if found

- **result** (object): 
- **success** (boolean): 

### 404

Not Found

- **errors** (array): 
- **success** (boolean):
