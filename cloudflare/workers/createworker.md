# Create Worker

`POST /accounts/{account_id}/workers/workers`

Create a new Worker.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **created_on** (string, optional): When the Worker was created.
- **deployed_on** (string, optional): When the Worker's most recent deployment was created. `null` if the Worker has never been deployed.
- **id** (string, optional): Immutable ID of the Worker.
- **logpush** (boolean, optional): Whether logpush is enabled for the Worker.
- **name** (string, optional): Name of the Worker.
- **observability** (object, optional): Observability settings for the Worker.
- **references** (object, optional): Other resources that reference the Worker and depend on it existing.
- **subdomain** (object, optional): Subdomain settings for the Worker.
- **tags** (array, optional): Tags associated with the Worker.
- **tail_consumers** (array, optional): Other Workers that should consume logs from the Worker.
- **updated_on** (string, optional): When the Worker was most recently updated.

## Response

### 200

Create Worker success.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 400

Bad Request - Invalid input data.

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

### 403

Forbidden - Access denied or limit exceeded.

- **errors** (array, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

### 409

Conflict - Resource already exists.

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
