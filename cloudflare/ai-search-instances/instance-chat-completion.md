# Chat Completions

`POST /accounts/{account_id}/ai-search/instances/{id}/chat/completions`

Performs a chat completion request against an AI Search instance, using indexed content as context for generating responses.

## Parameters

- **id** (string, required) [path]: AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores.
- **account_id** (string, required) [path]: 

## Request Body

- **ai_search_options** (object, optional): 
- **messages** (array, required): 
- **model** (object, optional): 
- **stream** (boolean, optional): 

## Response

### 200

Returns the chat completions results with retrieved files.

- **choices** (array): 
- **chunks** (array): 
- **id** (string): 
- **model** (string): 
- **object** (string): 

### 404

Not Found

- **errors** (array): 
- **success** (boolean):
