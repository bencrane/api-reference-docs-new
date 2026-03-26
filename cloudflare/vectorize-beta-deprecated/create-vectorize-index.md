# Create Vectorize Index (Deprecated)

`POST /accounts/{account_id}/vectorize/indexes`

> **Deprecated**

Creates and returns a new Vectorize Index.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **config** (object, required): 
- **description** (string, optional): Specifies the description of the index.
- **name** (string, required): 

## Response

### 200

Create Vectorize Index Response

- **result** (object, optional): 

### 4XX

Create Vectorize Index Failure Response

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
