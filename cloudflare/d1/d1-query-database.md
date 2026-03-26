# Query D1 Database

`POST /accounts/{account_id}/d1/database/{database_id}/query`

Returns the query result as an object.

## Parameters

- **account_id** (string, required) [path]: 
- **database_id** (string, required) [path]: 

## Request Body

One of: single query, multiple queries

## Response

### 200

Query response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `true`

### 4XX

Query response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful
