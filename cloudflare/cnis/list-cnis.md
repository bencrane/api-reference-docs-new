# List existing CNI objects

`GET /accounts/{account_id}/cni/cnis`



## Parameters

- **slot** (string, optional) [query]: If specified, only show CNIs associated with the specified slot
- **tunnel_id** (string, optional) [query]: If specified, only show cnis associated with the specified tunnel id
- **cursor** (integer, optional) [query]: 
- **limit** (integer, optional) [query]: 
- **account_id** (string, required) [path]: 

## Response

### 200

List of matching CNI objects

- **items** (array): 
- **next** (integer): 

### 400

Bad request

### 500

Internal server error
