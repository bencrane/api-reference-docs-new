# Update query

`PATCH /accounts/{account_id}/workers/observability/queries/{queryId}`

Update saved query.

## Parameters

- **queryId** (string, required) [path]: 

## Request Body

- **description** (string, required): 
- **name** (string, required): Query name
- **parameters** (object, required): 

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
