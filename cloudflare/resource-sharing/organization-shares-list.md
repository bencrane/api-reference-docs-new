# List organization shares

`GET /organizations/{organization_id}/shares`

Lists all organization shares.

## Parameters

- **organization_id** (string, required) [path]: 
- **status** (string, optional) [query]: Filter shares by status.
- **kind** (string, optional) [query]: Filter shares by kind.
- **target_type** (string, optional) [query]: Filter shares by target_type.
- **resource_types** (array, optional) [query]: Filter share resources by resource_types.
- **order** (string, optional) [query]: Order shares by values in the given field.
- **direction** (string, optional) [query]: Direction to sort objects.
- **page** (integer, optional) [query]: Page number.
- **per_page** (integer, optional) [query]: Number of objects to return per page.

## Response

### 200

List organization shares response.

_Empty object_

### 4XX

List organization shares response failure.

- **errors** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful.

### 5XX

List organization shares response failure.

- **errors** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful.
