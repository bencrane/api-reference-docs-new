# Update a proxy endpoint

`PATCH /accounts/{account_id}/gateway/proxy_endpoints/{proxy_endpoint_id}`

Update a configured Zero Trust Gateway proxy endpoint.

## Parameters

- **proxy_endpoint_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

- **ips** (array, optional): Specify the list of CIDRs to restrict ingress connections.
- **name** (string, optional): Specify the name of the proxy endpoint.

## Response

### 200

Returns an updated proxy endpoint response.

_Empty object_

### 4XX

Returns an updated proxy endpoint response failure.

_Empty object_
