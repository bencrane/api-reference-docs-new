# Update a list

`PUT /accounts/{account_id}/rules/lists/{list_id}`

Updates the description of a list.

## Parameters

- **list_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

- **description** (string, optional): An informative summary of the list.

## Response

### 200

Update a list response.

_Empty object_

### 4XX

Update a list response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
