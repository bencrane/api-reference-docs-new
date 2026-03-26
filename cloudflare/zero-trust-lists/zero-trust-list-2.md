# Patch Zero Trust list.

`PATCH /accounts/{account_id}/gateway/lists/{list_id}`

Appends or removes an item from a configured Zero Trust list.

## Parameters

- **list_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

- **append** (array, optional): Add items to the list.
- **remove** (array, optional): Lists of item values you want to remove.

## Response

### 200

Patch Zero Trust list response.

_Empty object_

### 4XX

Patch Zero Trust list response failure.

_Empty object_
