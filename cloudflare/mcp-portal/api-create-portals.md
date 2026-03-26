# Create a new MCP Portal

`POST /accounts/{account_id}/access/ai-controls/mcp/portals`

Creates a new MCP portal for managing AI tool access through Cloudflare Access.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **allow_code_mode** (boolean, optional): Allow remote code execution in Dynamic Workers (beta)
- **description** (string, optional): 
- **hostname** (string, required): 
- **id** (string, required): portal id
- **name** (string, required): 
- **secure_web_gateway** (boolean, optional): Route outbound MCP traffic through Zero Trust Secure Web Gateway
- **servers** (array, optional): 

## Response

### 201

Returns the created Object

- **result** (object): 
- **success** (boolean): 

### 400

Input Validation Error

- **errors** (array): 
- **success** (boolean):
