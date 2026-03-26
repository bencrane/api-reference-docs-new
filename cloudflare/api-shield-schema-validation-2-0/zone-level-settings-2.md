# Update zone level schema validation settings

`PUT /zones/{zone_id}/api_gateway/settings/schema_validation`

> **Deprecated**

Updates zone level schema validation settings on the zone

## Request Body

- **validation_default_mitigation_action** (string, required): The default mitigation action used when there is no mitigation action defined on the operation

Mitigation actions are as follows:

  * `log` - log request when request does not conform to schema
  * `block` - deny access to the site when request does not conform to schema

A special value of of `none` will skip running schema validation entirely for the request when there is no mitigation action defined on the operation
 Values: `none`, `log`, `block`
- **validation_override_mitigation_action** (string, optional): When set, this overrides both zone level and operation level mitigation actions.

  - `none` will skip running schema validation entirely for the request
  - `null` indicates that no override is in place

To clear any override, use the special value `disable_override` or `null`
 Values: `none`, `disable_override`, ``

## Response

### 200

Update zone level schema validation settings response

- **validation_default_mitigation_action** (string): The default mitigation action used when there is no mitigation action defined on the operation

Mitigation actions are as follows:

  * `log` - log request when request does not conform to schema
  * `block` - deny access to the site when request does not conform to schema

A special value of of `none` will skip running schema validation entirely for the request when there is no mitigation action defined on the operation

- **validation_override_mitigation_action** (string): When set, this overrides both zone level and operation level mitigation actions.

  - `none` will skip running schema validation entirely for the request
  - `null` indicates that no override is in place


### 4XX

Update zone level schema validation settings response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
