# Retrieve information about all schemas on a zone

`GET /zones/{zone_id}/api_gateway/user_schemas`

> **Deprecated**

Lists all OpenAPI schemas uploaded to API Shield for the zone, including their validation status and associated operations.

## Parameters

- **page** (integer, optional) [query]: Page number of paginated results.
- **per_page** (integer, optional) [query]: Maximum number of results per page.
- **omit_source** (boolean, optional) [query]: Omit the source-files of schemas and only retrieve their meta-data.
- **validation_enabled** (string, optional) [query]: 

## Response

### 200

Retrieve information about all schemas on a zone response

- **result** (array, optional): 

### 4XX

Retrieve information about all schemas on a zone response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
