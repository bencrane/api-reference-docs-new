# Convert an Access application policy to a reusable policy

`PUT /accounts/{account_id}/access/apps/{app_id}/policies/{policy_id}/make_reusable`

Converts an application-scoped policy to a reusable policy. The policy will no longer be exclusively scoped to the application. Further updates to the policy should go through the /accounts/{account_id}/policies/{uid} endpoint.

## Parameters

- **app_id** (string, required) [path]: The application ID.
- **policy_id** (string, required) [path]: The policy ID.
- **account_id** (string, required) [path]: 

## Response

### 200

Convert an Access application policy to a reusable policy

_Empty object_

### 4XX

Convert an Access application policy to a reusable policy failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
