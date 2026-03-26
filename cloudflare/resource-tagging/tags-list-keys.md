# List tag keys

`GET /accounts/{account_id}/tags/keys`

Lists all distinct tag keys used across resources in an account.

## Parameters

- **account_id** (string, required) [path]: 
- **cursor** (string, optional) [query]: Cursor for pagination.

## Response

### 200

List tag keys response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (array, optional): Contains an array of distinct tag keys.
- **result_info** (object, optional): 

### 4XX

List tag keys response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

### 5XX

List tag keys response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
