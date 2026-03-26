# Get Vectors By Identifier

`POST /accounts/{account_id}/vectorize/v2/indexes/{index_name}/get_by_ids`

Get a set of vectors from an index by their vector identifiers.

## Parameters

- **account_id** (string, required) [path]: 
- **index_name** (string, required) [path]: 

## Request Body

- **ids** (array, optional): A list of vector identifiers to retrieve from the index indicated by the path.

## Response

### 200

Get Vectors By Identifier Response

- **result** (array, optional): Array of vectors with matching ids.

### 4XX

Get Vectors By Identifier Failure Response

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
