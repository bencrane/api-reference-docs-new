# Delete a proxy endpoint

`DELETE /accounts/{account_id}/gateway/proxy_endpoints/{proxy_endpoint_id}`

Delete a configured Zero Trust Gateway proxy endpoint.

## Parameters

- **proxy_endpoint_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 


## Response

### 200

Returns a deleted proxy endpoint response.

_Empty object_

### 4XX

Returns a deleted proxy endpoint response failure.

_Empty object_
