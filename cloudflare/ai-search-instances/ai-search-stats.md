# Stats

`GET /accounts/{account_id}/ai-search/instances/{id}/stats`

Retrieves usage statistics for AI Search instances.

## Parameters

- **id** (string, required) [path]: AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores.
- **account_id** (string, required) [path]: 

## Response

### 200

Returns the AI Search stats.

- **result** (object): 
- **success** (boolean): 

### 404

Not Found

- **errors** (array): 
- **success** (boolean):
