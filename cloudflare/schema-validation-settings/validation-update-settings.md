# Update global schema validation settings

`PUT /zones/{zone_id}/schema_validation/settings`

Fully updates global schema validation settings for a zone, replacing existing configuration.

## Request Body

_Empty object_

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
