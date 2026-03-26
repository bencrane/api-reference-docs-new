# List per-operation schema validation settings

`GET /zones/{zone_id}/schema_validation/settings/operations`

Lists all per-operation schema validation settings configured for the zone.

## Parameters

- **page** (integer, optional) [query]: Page number of paginated results.
- **per_page** (integer, optional) [query]: Maximum number of results per page.

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
