# Create an IP Access rule

`POST /user/firewall/access_rules/rules`

Creates a new IP Access rule for all zones owned by the current user.

Note: To create an IP Access rule that applies to a specific zone, refer to the [IP Access rules for a zone](#ip-access-rules-for-a-zone) endpoints.

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
