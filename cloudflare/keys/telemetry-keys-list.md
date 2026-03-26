# List keys

`POST /accounts/{account_id}/workers/observability/telemetry/keys`

List all the keys in your telemetry events.

## Request Body

- **datasets** (array, optional): Leave this empty to use the default datasets
- **filters** (array, optional): Apply filters to narrow key discovery. Supports nested groups via kind: 'group'. Maximum nesting depth is 4.
- **from** (number, optional): 
- **keyNeedle** (object, optional): If the user suggests a key, use this to narrow down the list of keys returned. Make sure matchCase is false to avoid case sensitivity issues.
- **limit** (number, optional): Advanced usage: set limit=1000+ to retrieve comprehensive key options without needing additional filtering.
- **needle** (object, optional): Search for a specific substring in any of the events
- **to** (number, optional): 

## Response

### 200

Successful request

- **errors** (array): 
- **messages** (array): 
- **result** (array): 
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
