# Update all list items

`PUT /accounts/{account_id}/rules/lists/{list_id}/items`

Removes all existing items from the list and adds the provided items to the list.

This operation is asynchronous. To get current the operation status, invoke the `Get bulk operation status` endpoint with the returned `operation_id`.

There is a limit of 1 pending bulk operation per account. If an outstanding bulk operation is in progress, the request will be rejected.

## Parameters

- **list_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

Array of object

## Response

### 200

Update all list items response.

- **result** (object, optional): 

### 4XX

Update all list items response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
