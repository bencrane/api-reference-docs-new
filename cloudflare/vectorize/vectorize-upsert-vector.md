# Upsert Vectors

`POST /accounts/{account_id}/vectorize/v2/indexes/{index_name}/upsert`

Upserts vectors into the specified index, creating them if they do not exist and returns a mutation id corresponding to the vectors enqueued for upsertion.

## Parameters

- **account_id** (string, required) [path]: 
- **index_name** (string, required) [path]: 
- **unparsable-behavior** (string, optional) [query]: 


## Response

### 200

Upsert Vectors Response

- **result** (object, optional): 

### 4XX

Upsert Vectors Failure Response

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
