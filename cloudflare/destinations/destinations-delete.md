# Delete Destination

`DELETE /accounts/{account_id}/workers/observability/destinations/{slug}`

Delete a Workers Observability Telemetry Destination.

## Parameters

- **slug** (string, required) [path]: 

## Response

### 200

Successful request

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): 

### 401

Unauthorized

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): 

### 404

Not found

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): 

### 500

Internal error

- **errors** (array): 
- **messages** (array): 
- **success** (boolean):
