# List Permission Groups

`GET /accounts/{account_id}/tokens/permission_groups`

Find all available permission groups for Account Owned API Tokens

## Parameters

- **account_id** (string, required) [path]: 
- **name** (string, optional) [query]: Filter by the name of the permission group.
The value must be URL-encoded.
- **scope** (string, optional) [query]: Filter by the scope of the permission group.
The value must be URL-encoded.

## Response

### 200

List Account Owned API Token Permission Groups response

- **result** (array, optional): 

### 4XX

List Account Owned API Token Permission Groups response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
