# Delete a firewall rule

`DELETE /zones/{zone_id}/firewall/rules/{rule_id}`

> **Deprecated**

Deletes an existing firewall rule.

## Parameters

- **rule_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Request Body

- **delete_filter_if_unused** (boolean, optional): When true, indicates that Cloudflare should also delete the associated filter if there are no other firewall rules referencing the filter.

## Response

### 200

Delete a firewall rule response

- **result** (object, optional): 

### 4XX

Delete a firewall rule response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
