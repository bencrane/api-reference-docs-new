# Get Advertisement Status

`GET /accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/status`

> **Deprecated**

View the current advertisement state for a prefix.

**Deprecated:** Prefer the BGP Prefixes endpoints, which additionally allow for advertising and withdrawing 
subnets of an IP prefix.


## Parameters

- **prefix_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Get Advertisement Status response

- **result** (object, optional): 

### 4XX

Get Advertisement Status response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
