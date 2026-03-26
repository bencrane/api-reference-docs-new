# List tag values

`GET /accounts/{account_id}/tags/values/{tag_key}`

Lists all distinct values for a given tag key, optionally filtered by resource type.

## Parameters

- **account_id** (string, required) [path]: 
- **tag_key** (string, required) [path]: The tag key to retrieve values for.
- **type** (string, optional) [query]: Filter by resource type.
- **cursor** (string, optional) [query]: Cursor for pagination.

## Response

### 200

List tag values response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (array, optional): 
- **result_info** (object, optional): 

### 4XX

List tag values response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

### 5XX

List tag values response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
