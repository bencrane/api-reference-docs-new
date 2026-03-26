# Create a WAF override

`POST /zones/{zone_id}/firewall/waf/overrides`

> **Deprecated**

Creates a URI-based WAF override for a zone.

**Note:** Applies only to the [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **urls** (array, required): The URLs to include in the current WAF override. You can use wildcards. Each entered URL will be escaped before use, which means you can only use simple wildcard patterns.

## Response

### 200

Create a WAF override response

- **result** (object, optional): 

### 4XX

Create a WAF override response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
