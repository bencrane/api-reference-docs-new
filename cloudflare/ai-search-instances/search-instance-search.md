# Search

`POST /accounts/{account_id}/ai-search/instances/{id}/search`

Executes a semantic search query against an AI Search instance to find relevant indexed content.

## Parameters

- **id** (string, required) [path]: AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores.
- **account_id** (string, required) [path]: 

## Request Body

- **ai_search_options** (object, optional): 
- **messages** (array, required): 

## Response

### 200

Returns the search results.

- **result** (object): 
- **success** (boolean): 

### 404

Not Found

- **errors** (array): 
- **success** (boolean):
