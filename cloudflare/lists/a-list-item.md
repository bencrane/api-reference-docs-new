# Get a list item

`GET /accounts/{account_id}/rules/lists/{list_id}/items/{item_id}`

Fetches a list item in the list.

## Parameters

- **item_id** (string, required) [path]: 
- **list_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Get a list item response.

- **result** (object, optional): 
- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Defines whether the API call was successful. Values: `true`

### 4XX

Get a list item response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
