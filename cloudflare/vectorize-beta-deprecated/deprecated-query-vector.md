# Query Vectors (Deprecated)

`POST /accounts/{account_id}/vectorize/indexes/{index_name}/query`

> **Deprecated**

Finds vectors closest to a given vector in an index.

## Parameters

- **account_id** (string, required) [path]: 
- **index_name** (string, required) [path]: 

## Request Body

- **filter** (object, optional): A metadata filter expression used to limit nearest neighbor results.
- **returnMetadata** (boolean, optional): Whether to return the metadata associated with the closest vectors.
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
