# Delete Vectors By Identifier

`POST /accounts/{account_id}/vectorize/v2/indexes/{index_name}/delete_by_ids`

Delete a set of vectors from an index by their vector identifiers.

## Parameters

- **account_id** (string, required) [path]: 
- **index_name** (string, required) [path]: 

## Request Body

- **ids** (array, optional): A list of vector identifiers to delete from the index indicated by the path.

## Response

### 200

Delete Vector Identifiers Response

- **result** (object, optional): 

### 4XX

Delete Vector Identifiers Failure Response

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
