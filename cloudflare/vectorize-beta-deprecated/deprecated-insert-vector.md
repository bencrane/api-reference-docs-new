# Insert Vectors (Deprecated)

`POST /accounts/{account_id}/vectorize/indexes/{index_name}/insert`

> **Deprecated**

Inserts vectors into the specified index and returns the count of the vectors successfully inserted.

## Parameters

- **account_id** (string, required) [path]: 
- **index_name** (string, required) [path]: 


## Response

### 200

Insert Vectors Response

- **result** (object, optional): 

### 4XX

Insert Vectors Failure Response

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
