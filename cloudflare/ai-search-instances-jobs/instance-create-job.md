# Create new job

`POST /accounts/{account_id}/ai-search/instances/{id}/jobs`

Creates a new indexing job for an AI Search instance.

## Parameters

- **id** (string, required) [path]: AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores.
- **account_id** (string, required) [path]: 

## Request Body

- **description** (string, optional): 

## Response

### 200

Returns the AI Search job id.

- **result** (object): 
- **success** (boolean): 

### 400

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean): 

### 500

Internal Error.

- **errors** (array): 
- **success** (boolean):
