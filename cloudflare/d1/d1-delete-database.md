# Delete D1 Database

`DELETE /accounts/{account_id}/d1/database/{database_id}`

Deletes the specified D1 database.

## Parameters

- **account_id** (string, required) [path]: 
- **database_id** (string, required) [path]: 

## Response

### 200

Delete D1 database response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `true`

### 4XX

Delete D1 database response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful
