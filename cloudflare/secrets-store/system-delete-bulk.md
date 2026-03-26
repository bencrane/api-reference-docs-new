# Delete secrets (System)

`DELETE /system/accounts/{account_tag}/stores/{store_id}/secrets`

Deletes one or more secrets from a store managed by the calling service.
Returns 404 if the store doesn't exist or is not managed by the authenticated service.


## Parameters

- **account_tag** (string, required) [path]: Account tag identifier (e.g., '12a6ed19f349896cfbd6694ba3de8d31').
This is the account's external tag identifier, not the numeric account ID.

- **store_id** (string, required) [path]: 

## Request Body

Array of object

## Response

### 200

Secret detail

- **result** (array, optional): 

### 4XX

Delete secrets failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
