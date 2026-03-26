# List MCP Servers

`GET /accounts/{account_id}/access/ai-controls/mcp/servers`

Lists all MCP portals configured for the account.

## Parameters

- **account_id** (string, required) [path]: 
- **page** (integer, optional) [query]: 
- **per_page** (integer, optional) [query]: 
- **search** (string, optional) [query]: 

## Response

### 200

List objects

- **result** (array): 
- **success** (boolean): 

### 400

Bad Request

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
