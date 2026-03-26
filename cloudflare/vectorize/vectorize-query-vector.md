# Query Vectors

`POST /accounts/{account_id}/vectorize/v2/indexes/{index_name}/query`

Finds vectors closest to a given vector in an index.

## Parameters

- **account_id** (string, required) [path]: 
- **index_name** (string, required) [path]: 

## Request Body

- **filter** (object, optional): A metadata filter expression used to limit nearest neighbor results.
- **returnMetadata** (string, optional): Whether to return no metadata, indexed metadata or all metadata associated with the closest vectors. Values: `none`, `indexed`, `all`
- **returnValues** (boolean, optional): Whether to return the values associated with the closest vectors.
- **topK** (number, optional): The number of nearest neighbors to find.
- **vector** (array, required): The search vector that will be used to find the nearest neighbors.

## Response

### 200

Query Vectors Response

- **result** (object, optional): 

### 4XX

Query Vectors Failure Response

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
