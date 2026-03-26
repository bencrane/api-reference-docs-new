# Create an IP Access rule

`POST /zones/{zone_id}/firewall/access_rules/rules`

Creates a new IP Access rule for a zone.

Note: To create an IP Access rule that applies to multiple zones, refer to [IP Access rules for a user](#ip-access-rules-for-a-user) or [IP Access rules for an account](#ip-access-rules-for-an-account) as appropriate.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **configuration** (object, required): The rule configuration.
- **mode** (string, required): The action to apply to a matched request. Values: `block`, `challenge`, `whitelist`, `js_challenge`, `managed_challenge`
- **notes** (object, optional): 

## Response

### 200

Create an IP Access rule response.

- **result** (object, optional): 

### 4XX

Create an IP Access rule response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
