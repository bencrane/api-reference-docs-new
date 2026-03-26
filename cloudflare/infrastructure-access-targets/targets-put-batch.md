# Create new targets

`PUT /accounts/{account_id}/infrastructure/targets/batch`

Adds one or more targets.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

Array of object

## Response

### 200

Successfully created the targets

- **result** (array, optional): 

### 4XX

Failed to create the targets

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
