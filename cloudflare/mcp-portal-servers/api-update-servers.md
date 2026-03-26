# Update a MCP Server

`PUT /accounts/{account_id}/access/ai-controls/mcp/servers/{id}`

Updates an MCP portal configuration.

## Parameters

- **id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

- **auth_credentials** (string, optional): 
- **description** (string, optional): 
- **name** (string, optional): 

## Response

### 200

Returns the updated Object

- **result** (object): 
- **success** (boolean): 

### 400

Input Validation Error

- **errors** (array): 
- **success** (boolean): 

### 404

Not Found

- **errors** (array): 
- **success** (boolean):
