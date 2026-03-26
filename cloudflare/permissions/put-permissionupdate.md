# Update a permission for dataset

`PUT /accounts/{account_id}/cloudforce-one/events/dataset/{dataset_id}/permissions/{grant_id}`

Update a permission

## Parameters

- **account_id** (string, required) [path]: Account ID.
- **dataset_id** (string, required) [path]: Dataset UUID.
- **grant_id** (string, required) [path]: 

## Request Body

- **role** (string, required):  Values: `read`, `write`

## Response

### 200

Permission updated successfully

- **message** (string): 
- **success** (boolean): 

### 400

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean): 

### 404

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
