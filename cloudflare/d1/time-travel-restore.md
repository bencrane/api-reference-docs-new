# Restore D1 Database to a bookmark or point in time

`POST /accounts/{account_id}/d1/database/{database_id}/time_travel/restore`

Restores a D1 database to a previous point in time either via a bookmark or a timestamp.


## Parameters

- **account_id** (string, required) [path]: 
- **database_id** (string, required) [path]: 
- **bookmark** (string, optional) [query]: A bookmark to restore the database to. Required if `timestamp` is not provided.
- **timestamp** (string, optional) [query]: An ISO 8601 timestamp to restore the database to. Required if `bookmark` is not provided.

## Response

### 200

Database restored successfully

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): Response from a time travel restore operation.
- **success** (boolean, optional): Whether the API call was successful Values: `true`

### 4XX

Restore operation failed

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful
