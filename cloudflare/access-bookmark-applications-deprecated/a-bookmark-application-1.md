# Get a Bookmark application

`GET /accounts/{account_id}/access/bookmarks/{bookmark_id}`

> **Deprecated**

Fetches a single Bookmark application.

## Parameters

- **bookmark_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Get a Bookmark application response

_Empty object_

### 4XX

Get a Bookmark application response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
