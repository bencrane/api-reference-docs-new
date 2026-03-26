# List WAF overrides

`GET /zones/{zone_id}/firewall/waf/overrides`

> **Deprecated**

Fetches the URI-based WAF overrides in a zone.

**Note:** Applies only to the [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

## Parameters

- **zone_id** (string, required) [path]: 
- **page** (number, optional) [query]: 
- **per_page** (number, optional) [query]: 

## Response

### 200

List WAF overrides response

- **result** (array, optional): 

### 4XX

List WAF overrides response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
