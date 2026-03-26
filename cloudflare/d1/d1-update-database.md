# Update D1 Database

`PUT /accounts/{account_id}/d1/database/{database_id}`

Updates the specified D1 database.

## Parameters

- **account_id** (string, required) [path]: 
- **database_id** (string, required) [path]: 

## Request Body

- **read_replication** (object, required): Configuration for D1 read replication.

## Response

### 200

Database details response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): The details of the D1 database.
- **success** (boolean, optional): Whether the API call was successful Values: `true`

### 4XX

Update D1 database response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful
