# Update Zero Trust list

`PUT /accounts/{account_id}/gateway/lists/{list_id}`

Updates a configured Zero Trust list. Skips updating list items if not included in the payload. A non empty list items will overwrite the existing list.

## Parameters

- **list_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

- **description** (string, optional): Provide the list description.
- **items** (array, optional): Add items to the list.
- **name** (string, required): Specify the list name.

## Response

### 200

Update Zero Trust list response.

_Empty object_

### 4XX

Update Zero Trust list response failure.

_Empty object_
