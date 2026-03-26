# Update priority of a firewall rule

`PATCH /zones/{zone_id}/firewall/rules/{rule_id}`

> **Deprecated**

Updates the priority of an existing firewall rule.

## Parameters

- **rule_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Request Body

- **id** (string, required): The unique identifier of the resource.

## Response

### 200

Update priority of a firewall rule response

- **result** (array, optional): 

### 4XX

Update priority of a firewall rule response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
