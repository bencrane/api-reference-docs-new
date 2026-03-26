# Delete Worker

`DELETE /accounts/{account_id}/workers/workers/{worker_id}`

Delete a Worker and all its associated resources (versions, deployments, etc.).

## Parameters

- **account_id** (string, required) [path]: 
- **worker_id** (string, required) [path]: 

## Response

### 200

Delete Worker success.

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Whether the API call was successful.

### 400

Bad Request - Missing or invalid parameters.

- **errors** (array, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

### 401

Authentication required or insufficient permissions.

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
