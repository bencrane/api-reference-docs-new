# Raw D1 Database query

`POST /accounts/{account_id}/d1/database/{database_id}/raw`

Returns the query result rows as arrays rather than objects. This is a performance-optimized version of the /query endpoint.

## Parameters

- **account_id** (string, required) [path]: 
- **database_id** (string, required) [path]: 

## Request Body

One of: single query, multiple queries

## Response

### 200

Raw query response

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
