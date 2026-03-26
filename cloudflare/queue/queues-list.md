# List Queues

`GET /accounts/{account_id}/queues`

Returns the queues owned by an account.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

List of all Queues that belong to this account

_Empty object_

### 4XX

Failure response

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Indicates if the API call was successful or not.
