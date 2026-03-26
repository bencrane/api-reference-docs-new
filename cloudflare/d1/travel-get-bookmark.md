# Get D1 database bookmark

`GET /accounts/{account_id}/d1/database/{database_id}/time_travel/bookmark`

Retrieves the current bookmark, or the nearest bookmark at or before a provided timestamp.
Bookmarks can be used with the restore endpoint to revert the database to a previous point in time.


## Parameters

- **account_id** (string, required) [path]: 
- **database_id** (string, required) [path]: 
- **timestamp** (string, optional) [query]: An optional ISO 8601 timestamp. If provided, returns the nearest available bookmark at or before this timestamp. If omitted, returns the current bookmark.

## Response

### 200

Bookmark retrieved successfully

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `true`

### 4XX

Failed to retrieve bookmark

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful
