# Retrieve information about a specific schema on a zone

`GET /zones/{zone_id}/api_gateway/user_schemas/{schema_id}`

> **Deprecated**

Gets detailed information about a specific uploaded OpenAPI schema, including its contents and validation configuration.

## Parameters

- **omit_source** (boolean, optional) [query]: Omit the source-files of schemas and only retrieve their meta-data.

## Response

### 200

Retrieve information about a specific schema on a zone response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Retrieve information about a specific schema zone response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
