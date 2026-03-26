# Update a WAF rule

`PATCH /zones/{zone_id}/firewall/waf/packages/{package_id}/rules/{rule_id}`

> **Deprecated**

Updates a WAF rule. You can only update the mode/action of the rule.

**Note:** Applies only to the [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

## Parameters

- **rule_id** (string, required) [path]: 
- **package_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Request Body

- **mode** (string, optional): Defines the mode/action of the rule when triggered. You must use a value from the `allowed_modes` array of the current rule. Values: `default`, `disable`, `simulate`, `block`, `challenge`, `on`, `off`

## Response

### 200

Update a WAF rule response.

- **result** (object, optional): 

### 4XX

Update a WAF rule response failure.

- **result** (object, optional):  Values: ``
- **errors** (object, optional): 
- **messages** (object, optional): 
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
