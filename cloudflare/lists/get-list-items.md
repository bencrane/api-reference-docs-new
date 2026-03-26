# Get list items

`GET /accounts/{account_id}/rules/lists/{list_id}/items`

Fetches all the items in the list.

## Parameters

- **list_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 
- **cursor** (string, optional) [query]: 
- **per_page** (integer, optional) [query]: 
- **search** (string, optional) [query]: 

## Response

### 200

Get list items response.

- **result** (array, optional): 
- **result_info** (object, optional): 

### 4XX

Get list items response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
