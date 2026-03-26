# List Account Permission Groups

`GET /accounts/{account_id}/iam/permission_groups`

List all the permissions groups for an account.

## Parameters

- **account_id** (string, required) [path]: 
- **id** (string, optional) [query]: 
- **name** (string, optional) [query]: 
- **label** (string, optional) [query]: 
- **page** (number, optional) [query]: 
- **per_page** (number, optional) [query]: 

## Response

### 200

List Permission Groups response

- **result** (array, optional): A set of permission groups that are specified to the policy.

### 4XX

List Permission Groups response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
