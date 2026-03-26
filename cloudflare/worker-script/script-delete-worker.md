# Delete Worker

`DELETE /accounts/{account_id}/workers/scripts/{script_name}`

Delete your worker. This call has no response body on a successful delete.

## Parameters

- **account_id** (string, required) [path]: 
- **script_name** (string, required) [path]: 
- **force** (boolean, optional) [query]: If set to true, delete will not be stopped by associated service binding, durable object, or other binding. Any of these associated bindings/durable objects will be deleted along with the script.


## Response

### 200

Delete Worker response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional):  Values: ``

### 4XX

Delete Worker response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
