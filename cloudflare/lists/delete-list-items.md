# Delete list items

`DELETE /accounts/{account_id}/rules/lists/{list_id}/items`

Removes one or more items from a list.

This operation is asynchronous. To get current the operation status, invoke the `Get bulk operation status` endpoint with the returned `operation_id`.

There is a limit of 1 pending bulk operation per account. If an outstanding bulk operation is in progress, the request will be rejected.

## Parameters

- **list_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

- **items** (array, optional): 

## Response

### 200

Delete list items response.

- **result** (object, optional): 

### 4XX

Delete list items response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
