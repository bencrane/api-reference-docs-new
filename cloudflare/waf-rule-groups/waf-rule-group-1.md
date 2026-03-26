# Update a WAF rule group

`PATCH /zones/{zone_id}/firewall/waf/packages/{package_id}/groups/{group_id}`

> **Deprecated**

Updates a WAF rule group. You can update the state (`mode` parameter) of a rule group.

**Note:** Applies only to the [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

## Parameters

- **group_id** (string, required) [path]: 
- **package_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Request Body

- **mode** (string, optional): Defines the state of the rules contained in the rule group. When `on`, the rules in the group are configurable/usable. Values: `on`, `off`

## Response

### 200

Update a WAF rule group response.

- **result** (object, optional): 

### 4XX

Update a WAF rule group response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
