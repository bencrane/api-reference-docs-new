# Update a user seat

`PATCH /accounts/{account_id}/access/seats`

Removes a user from a Zero Trust seat when both `access_seat` and `gateway_seat` are set to false.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

Array of object

## Response

### 200

Update a user seat response

_Empty object_

### 4XX

Update a user seat response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
