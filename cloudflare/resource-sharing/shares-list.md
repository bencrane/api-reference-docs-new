# List account shares

`GET /accounts/{account_id}/shares`

Lists all account shares.

## Parameters

- **account_id** (string, required) [path]: 
- **status** (string, optional) [query]: Filter shares by status.
- **kind** (string, optional) [query]: Filter shares by kind.
- **target_type** (string, optional) [query]: Filter shares by target_type.
- **resource_types** (array, optional) [query]: Filter share resources by resource_types.
- **order** (string, optional) [query]: Order shares by values in the given field.
- **direction** (string, optional) [query]: Direction to sort objects.
- **page** (integer, optional) [query]: Page number.
- **per_page** (integer, optional) [query]: Number of objects to return per page.
- **include_resources** (boolean, optional) [query]: Include resources in the response.
- **include_recipient_counts** (boolean, optional) [query]: Include recipient counts in the response.

## Response

### 200

List account shares response.

_Empty object_

### 4XX

List account shares response failure.

- **errors** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful.

### 5XX

List account shares response failure.

- **errors** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful.
