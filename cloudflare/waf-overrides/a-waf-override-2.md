# Get a WAF override

`GET /zones/{zone_id}/firewall/waf/overrides/{overrides_id}`

> **Deprecated**

Fetches the details of a URI-based WAF override.

**Note:** Applies only to the [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

## Parameters

- **overrides_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Response

### 200

Get a WAF override response

- **result** (object, optional): 

### 4XX

Get a WAF override response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
