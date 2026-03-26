# Update a Bookmark application

`PUT /accounts/{account_id}/access/bookmarks/{bookmark_id}`

> **Deprecated**

Updates a configured Bookmark application.

## Parameters

- **bookmark_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 


## Response

### 200

Update a Bookmark application response

_Empty object_

### 4XX

Update a Bookmark application response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
