# Search

`POST /accounts/{account_id}/autorag/rags/{id}/search`



## Parameters

- **id** (string, required) [path]: rag id
- **account_id** (string, required) [path]: 

## Request Body

- **filters** (object, optional): 
- **max_num_results** (integer, optional): 
- **query** (string, required): 
- **ranking_options** (object, optional): 
- **reranking** (object, optional): 
- **rewrite_query** (boolean, optional): 

## Response

### 200

Returns the log details

- **result** (object): 
- **success** (boolean): 

### 404

Not Found

- **errors** (array): 
- **success** (boolean):
