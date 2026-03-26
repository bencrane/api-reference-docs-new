# List Events

`GET /accounts/{account_id}/magic/connectors/{connector_id}/telemetry/events`



## Parameters

- **account_id** (string, required) [path]: 
- **connector_id** (string, required) [path]: 
- **from** (number, required) [query]: 
- **to** (number, required) [query]: 
- **limit** (number, optional) [query]: 
- **cursor** (string, optional) [query]: 
- **k** (string, optional) [query]: Filter by event kind

## Response

### 200

OK

_Empty object_

### 400

Bad Request

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): 

### 401

Unauthorized

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): 

### 403

Forbidden

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): 

### 429

Too Many Requests

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): 

### 500

Internal Server Error

- **errors** (array): 
- **messages** (array): 
- **success** (boolean):
