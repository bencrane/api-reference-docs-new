# List hostname routes

`GET /accounts/{account_id}/zerotrust/routes/hostname`

Lists and filters hostname routes in an account.

## Parameters

- **account_id** (string, required) [path]: 
- **id** (string, optional) [query]: 
- **hostname** (string, optional) [query]: If set, only list hostname routes that contain a substring of the given value, the filter is case-insensitive.
- **tunnel_id** (string, optional) [query]: If set, only list hostname routes that point to a specific tunnel.
- **comment** (string, optional) [query]: 
- **existed_at** (string, optional) [query]: 
- **is_deleted** (boolean, optional) [query]: 
- **per_page** (string, optional) [query]: 
- **page** (string, optional) [query]: 

## Response

### 200

List hostname routes response

- **result** (array, optional): 

### 4XX

List hostname routes failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
