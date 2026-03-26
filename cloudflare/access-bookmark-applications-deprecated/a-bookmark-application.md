# Delete a Bookmark application

`DELETE /accounts/{account_id}/access/bookmarks/{bookmark_id}`

> **Deprecated**

Deletes a Bookmark application.

## Parameters

- **bookmark_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 


## Response

### 200

Delete a Bookmark application response

_Empty object_

### 4XX

Delete a Bookmark application response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
