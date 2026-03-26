# Delete Service Binding

`DELETE /accounts/{account_id}/addressing/prefixes/{prefix_id}/bindings/{binding_id}`

Delete a Service Binding

## Parameters

- **account_id** (string, required) [path]: 
- **prefix_id** (string, required) [path]: 
- **binding_id** (string, required) [path]: 

## Response

### 200

Service Binding deleted

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Whether the API call was successful.

### 4XX

Delete Service Binding response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
