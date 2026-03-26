# List Gateway Logs

`GET /accounts/{account_id}/ai-gateway/gateways/{gateway_id}/logs`



## Parameters

- **account_id** (string, required) [path]: 
- **gateway_id** (string, required) [path]: 
- **search** (string, optional) [query]: 
- **page** (integer, optional) [query]: 
- **per_page** (integer, optional) [query]: 
- **order_by** (string, optional) [query]: 
- **order_by_direction** (string, optional) [query]: 
- **filters** (array, optional) [query]: 
- **meta_info** (boolean, optional) [query]: 
- **direction** (string, optional) [query]: 
- **start_date** (string, optional) [query]: 
- **end_date** (string, optional) [query]: 
- **min_cost** (number, optional) [query]: 
- **max_cost** (number, optional) [query]: 
- **min_tokens_in** (number, optional) [query]: 
- **max_tokens_in** (number, optional) [query]: 
- **min_tokens_out** (number, optional) [query]: 
- **max_tokens_out** (number, optional) [query]: 
- **min_total_tokens** (number, optional) [query]: 
- **max_total_tokens** (number, optional) [query]: 
- **min_duration** (number, optional) [query]: 
- **max_duration** (number, optional) [query]: 
- **feedback** (string, optional) [query]: 
- **success** (boolean, optional) [query]: 
- **cached** (boolean, optional) [query]: 
- **model** (string, optional) [query]: 
- **model_type** (string, optional) [query]: 
- **provider** (string, optional) [query]: 
- **request_content_type** (string, optional) [query]: 
- **response_content_type** (string, optional) [query]: 

## Response

### 200

Returns a list of Gateway Logs

- **result** (array): 
- **result_info** (object): 
- **success** (boolean): 

### 400

Bad Request

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
