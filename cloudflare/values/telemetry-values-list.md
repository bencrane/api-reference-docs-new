# List values

`POST /accounts/{account_id}/workers/observability/telemetry/values`

List unique values found in your events.

## Request Body

- **datasets** (array, required): Leave this empty to use the default datasets
- **filters** (array, optional): Apply filters before listing values. Supports nested groups via kind: 'group'. Maximum nesting depth is 4.
- **key** (string, required): 
- **limit** (number, optional): 
- **needle** (object, optional): Search for a specific substring in the event.
- **timeframe** (object, required): 
- **type** (string, required):  Values: `string`, `boolean`, `number`

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
