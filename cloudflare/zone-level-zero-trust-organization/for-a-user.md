# Revoke all Access tokens for a user

`POST /zones/{zone_id}/access/organizations/revoke_user`

Revokes a user's access across all applications.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **email** (string, required): The email of the user to revoke.

## Response

### 200

Revoke all Access tokens for a user response

_Empty object_

### 4xx

Revoke all Access tokens for a user response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
