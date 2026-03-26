# Delete Metadata Index

`POST /accounts/{account_id}/vectorize/v2/indexes/{index_name}/metadata_index/delete`

Allow Vectorize to delete the specified metadata index.

## Parameters

- **account_id** (string, required) [path]: 
- **index_name** (string, required) [path]: 

## Request Body

- **propertyName** (string, required): Specifies the metadata property for which the index must be deleted.

## Response

### 200

Delete Metadata Index Response

- **result** (object, optional): 

### 4XX

Delete Metadata Index Failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
