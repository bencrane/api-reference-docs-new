# List WAF rule groups

`GET /zones/{zone_id}/firewall/waf/packages/{package_id}/groups`

> **Deprecated**

Fetches the WAF rule groups in a WAF package.

**Note:** Applies only to the [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

## Parameters

- **package_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 
- **mode** (string, optional) [query]: 
- **page** (number, optional) [query]: 
- **per_page** (number, optional) [query]: 
- **order** (string, optional) [query]: 
- **direction** (string, optional) [query]: 
- **match** (string, optional) [query]: 
- **name** (string, optional) [query]: 
- **rules_count** (number, optional) [query]: 

## Response

### 200

Defines the list WAF rule groups response.

- **result** (array, optional): 

### 4XX

Defines the list WAF rule groups response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
