# Revoke all Access tokens for a user

`POST /accounts/{account_id}/access/organizations/revoke_user`

Revokes a user's access across all applications.

## Parameters

- **account_id** (string, required) [path]: 
- **devices** (boolean, optional) [query]: When set to `true`, all devices associated with the user will be revoked.

## Request Body

- **devices** (boolean, optional): When set to `true`, all devices associated with the user will be revoked.
- **email** (string, required): The email of the user to revoke.
- **user_uid** (string, optional): The uuid of the user to revoke.
- **warp_session_reauth** (boolean, optional): When set to `true`, the user will be required to re-authenticate to WARP for all Gateway policies that enforce a WARP client session duration. When `false`, the user’s WARP session will remain active

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
