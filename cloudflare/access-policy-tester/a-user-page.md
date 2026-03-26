# Get an Access policy test users page

`GET /accounts/{account_id}/access/policy-tests/{policy_test_id}/users`

Fetches a single page of user results from an Access policy test.

## Parameters

- **account_id** (string, required) [path]: 
- **policy_test_id** (string, required) [path]: 
- **page** (integer, optional) [query]: 
- **per_page** (integer, optional) [query]: 
- **status** (string, optional) [query]: Filter users by their policy evaluation status.

## Response

### 200

Get an Access policy tester users page response.

_Empty object_

### 400

Get an Access policy tester users page response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
