# Delete instances.

`DELETE /accounts/{account_id}/ai-search/instances/{id}`

Delete instances.

## Parameters

- **id** (string, required) [path]: AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores.
- **account_id** (string, required) [path]: 

## Response

### 200

Returns the Object if it was successfully deleted

- **result** (object): 
- **success** (boolean): 

### 404

Not Found

- **errors** (array): 
- **success** (boolean):
