# Create a Bookmark application

`POST /accounts/{account_id}/access/bookmarks/{bookmark_id}`

> **Deprecated**

Create a new Bookmark application.

## Parameters

- **bookmark_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 


## Response

### 200

Create a Bookmark application response

_Empty object_

### 4XX

Create a Bookmark application response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
