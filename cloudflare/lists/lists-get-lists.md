# Get lists

`GET /accounts/{account_id}/rules/lists`

Fetches all lists in the account.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

Get lists response.

_Empty object_

### 4XX

Get lists response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
