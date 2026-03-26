# List all uploaded schemas

`GET /zones/{zone_id}/schema_validation/schemas`

Lists all OpenAPI schemas uploaded to API Shield with pagination support.

## Parameters

- **page** (integer, optional) [query]: Page number of paginated results.
- **per_page** (integer, optional) [query]: Maximum number of results per page.
- **omit_source** (boolean, optional) [query]: Omit the source-files of schemas and only retrieve their meta-data.
- **validation_enabled** (boolean, optional) [query]: Filter for enabled schemas

## Response

### 200

Success

- **result** (array, optional): 

### 4XX

Failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
