# Get Worker

`GET /accounts/{account_id}/workers/workers/{worker_id}`

Get details about a specific Worker.

## Parameters

- **account_id** (string, required) [path]: 
- **worker_id** (string, required) [path]: 

## Response

### 200

Get Worker success.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 400

Bad Request - Missing or invalid parameters.

- **errors** (array, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

### 404

Not Found - Worker does not exist.

- **errors** (array, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

### 500

Internal Server Error - An unexpected server error occurred.

- **errors** (array, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
