# Author Search

`GET /accounts/{account_id}/ai/authors/search`

Searches Workers AI models by author or organization name.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

Returns a list of authors

- **errors** (array): 
- **messages** (array): 
- **result** (array): 
- **success** (boolean): 

### 400

Bad Request

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
