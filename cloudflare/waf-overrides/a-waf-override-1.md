# Delete a WAF override

`DELETE /zones/{zone_id}/firewall/waf/overrides/{overrides_id}`

> **Deprecated**

Deletes an existing URI-based WAF override.

**Note:** Applies only to the [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

## Parameters

- **overrides_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 


## Response

### 200

Delete a WAF override response

- **result** (object): 

### 4XX

Delete a WAF override response failure

- **result** (object, optional):  Values: ``
- **errors** (object, optional): 
- **messages** (object, optional): 
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
