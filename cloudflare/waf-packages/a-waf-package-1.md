# Update a WAF package

`PATCH /zones/{zone_id}/firewall/waf/packages/{package_id}`

> **Deprecated**

Updates a WAF package. You can update the sensitivity and the action of an anomaly detection WAF package.

**Note:** Applies only to the [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

## Parameters

- **package_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Request Body

- **action_mode** (string, optional): The default action performed by the rules in the WAF package. Values: `simulate`, `block`, `challenge`
- **sensitivity** (string, optional): The sensitivity of the WAF package. Values: `high`, `medium`, `low`, `off`

## Response

### 200

Update a WAF package response

- **result** (object, optional): 

### 4XX

Update a WAF package response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
