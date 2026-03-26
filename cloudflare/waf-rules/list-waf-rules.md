# List WAF rules

`GET /zones/{zone_id}/firewall/waf/packages/{package_id}/rules`

> **Deprecated**

Fetches WAF rules in a WAF package.

**Note:** Applies only to the [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

## Parameters

- **package_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 
- **mode** (string, optional) [query]: 
- **group_id** (string, optional) [query]: 
- **page** (number, optional) [query]: 
- **per_page** (number, optional) [query]: 
- **order** (string, optional) [query]: 
- **direction** (string, optional) [query]: 
- **match** (string, optional) [query]: 
- **description** (string, optional) [query]: 
- **priority** (string, optional) [query]: 

## Response

### 200

List WAF rules response.

- **result** (array, optional): 

### 4XX

List WAF rules response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
