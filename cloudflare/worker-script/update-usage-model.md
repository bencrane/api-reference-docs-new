# Update Usage Model

`PUT /accounts/{account_id}/workers/scripts/{script_name}/usage-model`

Updates the Usage Model for a given Worker. Requires a Workers Paid subscription.

## Parameters

- **account_id** (string, required) [path]: 
- **script_name** (string, required) [path]: 

## Request Body

- **usage_model** (string, optional): Usage model for the Worker invocations. Values: `standard`, `bundled`, `unbound`
- **user_limits** (object, optional): User-defined resource limits for Workers with standard usage model.

## Response

### 200

Update Usage Model response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Update Usage Model response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
