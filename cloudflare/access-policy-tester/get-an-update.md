# Get the current status of a given Access policy test

`GET /accounts/{account_id}/access/policy-tests/{policy_test_id}`

Fetches the current status of a given Access policy test.

## Parameters

- **account_id** (string, required) [path]: 
- **policy_test_id** (string, required) [path]: 

## Response

### 200

Get an Access policy test update response.

_Empty object_

### 400

Get an Access policy test update response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
