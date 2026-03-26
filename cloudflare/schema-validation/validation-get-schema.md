# Get details of a schema

`GET /zones/{zone_id}/schema_validation/schemas/{schema_id}`

Gets the contents and metadata of a specific OpenAPI schema uploaded to API Shield.

## Parameters

- **omit_source** (boolean, optional) [query]: Omit the source-files of schemas and only retrieve their meta-data.

## Response

### 200

Success

_Empty object_

### 4XX

Failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
