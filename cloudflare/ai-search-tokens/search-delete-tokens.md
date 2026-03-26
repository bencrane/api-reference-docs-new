# Delete tokens.

`DELETE /accounts/{account_id}/ai-search/tokens/{id}`

Delete tokens.

## Parameters

- **account_id** (string, required) [path]: 
- **id** (string, required) [path]: 

## Response

### 200

Returns the Object if it was successfully deleted

- **result** (object): 
- **success** (boolean): 

### 404

Not Found

- **errors** (array): 
- **success** (boolean):
