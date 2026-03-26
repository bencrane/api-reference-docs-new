# Create Metadata Index

`POST /accounts/{account_id}/vectorize/v2/indexes/{index_name}/metadata_index/create`

Enable metadata filtering based on metadata property. Limited to 10 properties.

## Parameters

- **account_id** (string, required) [path]: 
- **index_name** (string, required) [path]: 

## Request Body

- **indexType** (string, required): Specifies the type of metadata property to index. Values: `string`, `number`, `boolean`
- **propertyName** (string, required): Specifies the metadata property to index.

## Response

### 200

Create Metadata Index Response

- **result** (object, optional): 

### 4XX

Create Metadata Index Failure Response

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
