# Create a new MCP Server

`POST /accounts/{account_id}/access/ai-controls/mcp/servers`

Creates a new MCP portal for managing AI tool access through Cloudflare Access.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **auth_credentials** (string, optional): 
- **auth_type** (string, required):  Values: `oauth`, `bearer`, `unauthenticated`
- **description** (string, optional): 
- **hostname** (string, required): 
- **id** (string, required): server id
- **name** (string, required): 

## Response

### 201

Returns the created Object

- **result** (object): 
- **success** (boolean): 

### 400

Input Validation Error

- **errors** (array): 
- **success** (boolean):
