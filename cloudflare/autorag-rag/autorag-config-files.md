# Files

`GET /accounts/{account_id}/autorag/rags/{id}/files`



## Parameters

- **id** (string, required) [path]: rag id
- **account_id** (string, required) [path]: 
- **page** (integer, optional) [query]: 
- **per_page** (integer, optional) [query]: 
- **search** (string, optional) [query]: 
- **status** (string, optional) [query]: 

## Response

### 200

Returns the AI Search files

- **result** (array): 
- **result_info** (object): 
- **success** (boolean): 

### 404

autorag_not_found

- **errors** (array): 
- **success** (boolean): 

### 503

unable_to_connect_to_autorag

- **errors** (array): 
- **success** (boolean):
