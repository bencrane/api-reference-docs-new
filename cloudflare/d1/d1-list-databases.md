# List D1 Databases

`GET /accounts/{account_id}/d1/database`

Returns a list of D1 databases.

## Parameters

- **account_id** (string, required) [path]: 
- **name** (string, optional) [query]: 
- **page** (number, optional) [query]: 
- **per_page** (number, optional) [query]: 

## Response

### 200

List D1 databases response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `true`
- **result_info** (object, optional): 

### 4XX

List D1 databases response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful
