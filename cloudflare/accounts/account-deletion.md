# Delete a specific account

`DELETE /accounts/{account_id}`

Delete a specific account (only available for tenant admins at this time). This is a permanent operation that will delete any zones or other resources under the account

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

Account Deletion Success Response

_Empty object_

### 4XX

Account Deletion Failure Response

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
