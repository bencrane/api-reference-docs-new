# Retrieve zone level schema validation settings

`GET /zones/{zone_id}/api_gateway/settings/schema_validation`

> **Deprecated**

Retrieves zone level schema validation settings currently set on the zone

## Response

### 200

Zone level schema validation settings response

- **validation_default_mitigation_action** (string): The default mitigation action used when there is no mitigation action defined on the operation

Mitigation actions are as follows:

  * `log` - log request when request does not conform to schema
  * `block` - deny access to the site when request does not conform to schema

A special value of of `none` will skip running schema validation entirely for the request when there is no mitigation action defined on the operation

- **validation_override_mitigation_action** (string): When set, this overrides both zone level and operation level mitigation actions.

  - `none` will skip running schema validation entirely for the request
  - `null` indicates that no override is in place


### 4XX

Zone level schema validation settings response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
