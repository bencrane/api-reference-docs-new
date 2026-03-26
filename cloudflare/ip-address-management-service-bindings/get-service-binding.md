# Get Service Binding

`GET /accounts/{account_id}/addressing/prefixes/{prefix_id}/bindings/{binding_id}`

Fetch a single Service Binding

## Parameters

- **account_id** (string, required) [path]: 
- **prefix_id** (string, required) [path]: 
- **binding_id** (string, required) [path]: 

## Response

### 200

The Service Binding with the requested ID

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Get Service Binding response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
