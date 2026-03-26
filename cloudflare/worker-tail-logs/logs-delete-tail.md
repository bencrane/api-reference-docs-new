# Delete Tail

`DELETE /accounts/{account_id}/workers/scripts/{script_name}/tails/{id}`

Deletes a tail from a Worker.

## Parameters

- **account_id** (string, required) [path]: 
- **script_name** (string, required) [path]: 
- **id** (string, required) [path]: 


## Response

### 200

Delete Tail response.

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Whether the API call was successful.

### 4XX

Delete Tail response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
