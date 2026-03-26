# List queries

`GET /accounts/{account_id}/workers/observability/queries`

List saved queries.

## Parameters

- **page** (number, optional) [query]: 
- **perPage** (number, optional) [query]: 
- **order** (string, optional) [query]: 
- **orderBy** (string, optional) [query]: 

## Response

### 200

Successful request

- **errors** (array): 
- **messages** (array): 
- **result** (array): 
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
