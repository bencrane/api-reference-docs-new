# Delete a device settings profile

`DELETE /accounts/{account_id}/devices/policy/{policy_id}`

Deletes a device settings profile and fetches a list of the remaining profiles for an account.

## Parameters

- **policy_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 


## Response

### 200

Delete a device settings profile response.

- **result** (array, optional): 

### 4XX

Delete a device settings profile response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
