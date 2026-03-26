# Create a proxy endpoint

`POST /accounts/{account_id}/gateway/proxy_endpoints`

Create a new Zero Trust Gateway proxy endpoint.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **kind** (string, optional): The proxy endpoint kind. Values: `ip`, `identity`

## Response

### 200

Returns a created proxy endpoint response.

_Empty object_

### 4XX

Returns a created proxy endpoint response failure.

_Empty object_
