# List Datasets

`GET /accounts/{account_id}/ai-gateway/gateways/{gateway_id}/datasets`

Lists all AI Gateway evaluator types configured for the account.

## Parameters

- **account_id** (string, required) [path]: 
- **gateway_id** (string, required) [path]: 
- **page** (integer, optional) [query]: 
- **per_page** (integer, optional) [query]: 
- **name** (string, optional) [query]: 
- **enable** (boolean, optional) [query]: 
- **search** (string, optional) [query]: 

## Response

### 200

List objects

- **result** (array): 
- **success** (boolean): 

### 400

Bad Request

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
