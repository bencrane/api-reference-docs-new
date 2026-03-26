# Deactivate a Zero Trust certificate

`POST /accounts/{account_id}/gateway/certificates/{certificate_id}/deactivate`

Unbind a single Zero Trust certificate from the edge.

## Parameters

- **certificate_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 


## Response

### 201

Deactivate Zero Trust certificate details response.

_Empty object_

### 4XX

Deactivate Zero Trust certificate details response failure.

_Empty object_
