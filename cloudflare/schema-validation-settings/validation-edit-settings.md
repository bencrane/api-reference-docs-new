# Edit global schema validation settings

`PATCH /zones/{zone_id}/schema_validation/settings`

Partially updates global schema validation settings for a zone using PATCH semantics.

## Request Body

- **validation_default_mitigation_action** (string, optional): The default mitigation action used
Mitigation actions are as follows:

  - `"log"` - log request when request does not conform to schema
  - `"block"` - deny access to the site when request does not conform to schema
  - `"none"` - skip running schema validation
 Values: `none`, `log`, `block`
- **validation_override_mitigation_action** (string, optional): When set, this overrides both zone level and operation level mitigation actions.

  - `"none"` - skip running schema validation entirely for the request
  - `null` - clears any existing override
 Values: `none`, ``

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
