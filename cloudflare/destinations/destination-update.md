# Update Destination

`PATCH /accounts/{account_id}/workers/observability/destinations/{slug}`

Update an existing Workers Observability Telemetry Destination.

## Parameters

- **slug** (string, required) [path]: 

## Request Body

- **configuration** (object, required): 
- **enabled** (boolean, required): 

## Response

### 200

Successful request

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): 

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
