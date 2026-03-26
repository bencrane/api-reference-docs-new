# List Jobs

`GET /accounts/{account_id}/autorag/rags/{id}/jobs`



## Parameters

- **id** (string, required) [path]: rag id
- **account_id** (string, required) [path]: 
- **page** (integer, optional) [query]: 
- **per_page** (integer, optional) [query]: 

## Response

### 200

Returns a list of AutoRAG Jobs

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
