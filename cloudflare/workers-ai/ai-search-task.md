# Task Search

`GET /accounts/{account_id}/ai/tasks/search`

Searches Workers AI models by task type (e.g., text-generation, embeddings).

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

Returns a list of tasks

- **errors** (array): 
- **messages** (array): 
- **result** (array): 
- **success** (boolean): 

### 404

Object not found

- **errors** (array): 
- **success** (boolean):
