# Delete Silence

`DELETE /accounts/{account_id}/alerting/v3/silences/{silence_id}`

Deletes an existing silence for an account.

## Parameters

- **account_id** (string, required) [path]: 
- **silence_id** (string, required) [path]: 

## Response

### 200

Delete Silence response

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Whether the API call was successful

### 4XX

Delete Silence response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `false`
