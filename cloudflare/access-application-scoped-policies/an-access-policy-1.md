# Delete an Access application policy

`DELETE /accounts/{account_id}/access/apps/{app_id}/policies/{policy_id}`

Deletes an Access policy specific to an application. To delete a reusable policy, use the /accounts/{account_id}/policies/{uid} endpoint.

## Parameters

- **app_id** (string, required) [path]: The application ID.
- **policy_id** (string, required) [path]: The policy ID.
- **account_id** (string, required) [path]: 

## Response

### 202

Delete an Access application policy response.

_Empty object_

### 4XX

Delete an Access application policy response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
