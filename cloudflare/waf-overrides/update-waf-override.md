# Update WAF override

`PUT /zones/{zone_id}/firewall/waf/overrides/{overrides_id}`

> **Deprecated**

Updates an existing URI-based WAF override.

**Note:** Applies only to the [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

## Parameters

- **overrides_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Request Body

- **id** (string, required): Defines an identifier.
- **rewrite_action** (object, required): Specifies that, when a WAF rule matches, its configured action will be replaced by the action configured in this object.
- **rules** (object, required): An object that allows you to override the action of specific WAF rules. Each key of this object must be the ID of a WAF rule, and each value must be a valid WAF action. Unless you are disabling a rule, ensure that you also enable the rule group that this WAF rule belongs to. When creating a new URI-based WAF override, you must provide a `groups` object or a `rules` object.
- **urls** (array, required): The URLs to include in the current WAF override. You can use wildcards. Each entered URL will be escaped before use, which means you can only use simple wildcard patterns.

## Response

### 200

Update WAF override response

- **result** (object, optional): 

### 4XX

Update WAF override response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
