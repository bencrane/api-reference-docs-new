# Create a store (System)

`POST /system/accounts/{account_tag}/stores`

Creates a store in the account on behalf of the calling service.
The store will be marked as managed by the authenticated service.
Requires account_id in the request body.


## Parameters

- **account_tag** (string, required) [path]: Account tag identifier (e.g., '12a6ed19f349896cfbd6694ba3de8d31').
This is the account's external tag identifier, not the numeric account ID.


## Request Body

- **account_id** (integer, required): Account internal ID (numeric). Required for system API routes.
This value must remain consistent for all stores within an account
managed by the same service.

- **name** (string, required): The name of the store

## Response

### 200

Store details

- **result** (object, optional): 

### 4XX

Create store failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
