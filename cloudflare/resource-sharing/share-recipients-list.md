# List share recipients by share ID

`GET /accounts/{account_id}/shares/{share_id}/recipients`

List share recipients by share ID.

## Parameters

- **account_id** (string, required) [path]: 
- **share_id** (string, required) [path]: 
- **include_resources** (boolean, optional) [query]: Include resources in the response.
- **page** (integer, optional) [query]: Page number.
- **per_page** (integer, optional) [query]: Number of objects to return per page.

## Response

### 200

List account share recipients response.

_Empty object_

### 4XX

List account share recipients response failure.

- **errors** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful.

### 5XX

List account share recipients response failure.

- **errors** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful.
