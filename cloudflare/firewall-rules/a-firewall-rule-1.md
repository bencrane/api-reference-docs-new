# Get a firewall rule

`GET /zones/{zone_id}/firewall/rules/{rule_id}`

> **Deprecated**

Fetches the details of a firewall rule.

## Parameters

- **rule_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 
- **id** (string, optional) [query]: 

## Response

### 200

Get a firewall rule response

- **result** (object, optional): 

### 4XX

Get a firewall rule response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
