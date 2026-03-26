# Update a MCP Portal

`PUT /accounts/{account_id}/access/ai-controls/mcp/portals/{id}`

Updates an MCP portal configuration.

## Parameters

- **id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

- **allow_code_mode** (boolean, optional): Allow remote code execution in Dynamic Workers (beta)
- **description** (string, optional): 
- **hostname** (string, optional): 
- **name** (string, optional): 
- **secure_web_gateway** (boolean, optional): Route outbound MCP traffic through Zero Trust Secure Web Gateway
- **servers** (array, optional): 

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
