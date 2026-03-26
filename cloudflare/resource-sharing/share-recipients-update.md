# Update a share's recipients

`PUT /accounts/{account_id}/shares/{share_id}/recipients`

Changes a share's recipients to match the given list. Returns an error if the share targets an organization.

## Parameters

- **account_id** (string, required) [path]: 
- **share_id** (string, required) [path]: 

## Request Body

Array of object

## Response

### 204

Empty body

### 4XX

Update share recipients failure.

- **errors** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful.

### 5XX

Update share recipients failure.

- **errors** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful.
