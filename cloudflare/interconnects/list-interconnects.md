# List existing interconnects

`GET /accounts/{account_id}/cni/interconnects`



## Parameters

- **site** (string, optional) [query]: If specified, only show interconnects located at the given site
- **type** (string, optional) [query]: If specified, only show interconnects of the given type
- **cursor** (integer, optional) [query]: 
- **limit** (integer, optional) [query]: 
- **account_id** (string, required) [path]: 

## Response

### 200

List of matching interconnect objects

- **items** (array): 
- **next** (integer): 

### 400

Bad request

### 500

Internal server error
