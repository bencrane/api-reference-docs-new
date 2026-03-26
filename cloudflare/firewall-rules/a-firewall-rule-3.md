# Update a firewall rule

`PUT /zones/{zone_id}/firewall/rules/{rule_id}`

> **Deprecated**

Updates an existing firewall rule.

## Parameters

- **rule_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Request Body

- **action** (object, required): The action to perform when the threshold of matched traffic within the configured period is exceeded.
- **filter** (object, required): 
- **id** (string, required): The unique identifier of the resource.

## Response

### 200

Update a firewall rule response

- **result** (object, optional): 

### 4XX

Update a firewall rule response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
