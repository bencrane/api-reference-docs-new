# Create Destination

`POST /accounts/{account_id}/workers/observability/destinations`

Create a new Workers Observability Telemetry Destination.

## Request Body

- **configuration** (object, required): 
- **enabled** (boolean, required): 
- **name** (string, required): 
- **skipPreflightCheck** (boolean, optional): 

## Response

### 201

Resource created

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

### 500

Internal error

- **errors** (array): 
- **messages** (array): 
- **success** (boolean):
