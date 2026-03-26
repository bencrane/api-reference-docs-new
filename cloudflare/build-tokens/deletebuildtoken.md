# Delete build token

`DELETE /accounts/{account_id}/builds/tokens/{build_token_uuid}`

Remove a build authentication token

## Parameters

- **account_id** (string, required) [path]: 
- **build_token_uuid** (string, required) [path]: 

## Response

### 200

Operation successful

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **result_info** (object): 
- **success** (boolean): 

### 404

Resource not found

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean):
