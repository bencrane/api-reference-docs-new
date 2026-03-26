# List WAF packages

`GET /zones/{zone_id}/firewall/waf/packages`

> **Deprecated**

Fetches WAF packages for a zone.

**Note:** Applies only to the [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

## Parameters

- **zone_id** (string, required) [path]: 
- **page** (number, optional) [query]: 
- **per_page** (number, optional) [query]: 
- **order** (string, optional) [query]: 
- **direction** (string, optional) [query]: 
- **match** (string, optional) [query]: 
- **name** (string, optional) [query]: 

## Response

### 200

List WAF packages response

Type: object

### 4XX

List WAF packages response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
