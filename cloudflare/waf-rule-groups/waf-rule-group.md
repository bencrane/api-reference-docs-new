# Get a WAF rule group

`GET /zones/{zone_id}/firewall/waf/packages/{package_id}/groups/{group_id}`

> **Deprecated**

Fetches the details of a WAF rule group.

**Note:** Applies only to the [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

## Parameters

- **group_id** (string, required) [path]: 
- **package_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Response

### 200

Get a WAF rule group response.

- **result** (object, optional): 

### 4XX

Get a WAF rule group response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
