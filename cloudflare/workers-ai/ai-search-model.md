# Model Search

`GET /accounts/{account_id}/ai/models/search`

Searches Workers AI models by name or description.

## Parameters

- **account_id** (string, required) [path]: 
- **per_page** (integer, optional) [query]: 
- **page** (integer, optional) [query]: 
- **task** (string, optional) [query]: Filter by Task Name
- **author** (string, optional) [query]: Filter by Author
- **source** (number, optional) [query]: Filter by Source Id
- **hide_experimental** (boolean, optional) [query]: Filter to hide experimental models
- **search** (string, optional) [query]: Search

## Response

### 200

Returns a list of models

- **errors** (array): 
- **messages** (array): 
- **result** (array): 
- **success** (boolean): 

### 404

Object not found

- **errors** (array): 
- **success** (boolean):
