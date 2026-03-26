# Upsert Vectors (Deprecated)

`POST /accounts/{account_id}/vectorize/indexes/{index_name}/upsert`

> **Deprecated**

Upserts vectors into the specified index, creating them if they do not exist and returns the count of values and ids successfully inserted.

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
