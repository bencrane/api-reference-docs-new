# Delete a MCP Server

`DELETE /accounts/{account_id}/access/ai-controls/mcp/servers/{id}`

Deletes an MCP portal from the account.

## Parameters

- **account_id** (string, required) [path]: 
- **id** (string, required) [path]: 

## Response

### 200

Returns the Object if it was successfully deleted

- **result** (object): 
- **success** (boolean): 

### 404

Not Found

- **errors** (array): 
- **success** (boolean):
