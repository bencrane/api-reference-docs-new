# Get D1 Database

`GET /accounts/{account_id}/d1/database/{database_id}`

Returns the specified D1 database.

## Parameters

- **account_id** (string, required) [path]: 
- **database_id** (string, required) [path]: 

## Response

### 200

Database details response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): The details of the D1 database.
- **success** (boolean, optional): Whether the API call was successful Values: `true`

### 4XX

Database details response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful
