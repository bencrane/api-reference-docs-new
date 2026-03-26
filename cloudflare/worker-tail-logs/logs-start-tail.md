# Start Tail

`POST /accounts/{account_id}/workers/scripts/{script_name}/tails`

Starts a tail that receives logs and exception from a Worker.

## Parameters

- **account_id** (string, required) [path]: 
- **script_name** (string, required) [path]: 


## Response

### 200

Start Tail response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Start Tail response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
