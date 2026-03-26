# List Evaluators

`GET /accounts/{account_id}/ai-gateway/evaluation-types`



## Parameters

- **account_id** (string, required) [path]: 
- **page** (integer, optional) [query]: 
- **per_page** (integer, optional) [query]: 
- **order_by** (string, optional) [query]: 
- **order_by_direction** (string, optional) [query]: 

## Response

### 200

Returns a list of Evaluators

- **result** (array): 
- **result_info** (object): 
- **success** (boolean): 

### 400

Bad Request

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
