# Upload a schema

`POST /zones/{zone_id}/schema_validation/schemas`

Uploads a new OpenAPI schema for API Shield schema validation. The schema defines expected request/response formats for API endpoints.

## Request Body

- **kind** (string, required): The kind of the schema Values: `openapi_v3`
- **name** (string, required): A human-readable name for the schema
- **source** (string, required): The raw schema, e.g., the OpenAPI schema, either as JSON or YAML
- **validation_enabled** (boolean, required): An indicator if this schema is enabled

## Response

### 200

Successfully uploaded the schema

_Empty object_

### 4XX

Failed uploaded the schema

_Empty object_
