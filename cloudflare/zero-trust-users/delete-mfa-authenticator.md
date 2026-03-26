# Delete a user's MFA device

`DELETE /accounts/{account_id}/access/users/{user_id}/mfa_authenticators/{authenticator_id}`

Deletes a specific MFA device for a user. This action is only available if MFA is turned on for the organization.

## Parameters

- **user_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 
- **authenticator_id** (string, required) [path]: 

## Response

### 200

Delete authenticator response.

_Empty object_

### 4XX

Delete authenticator response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
