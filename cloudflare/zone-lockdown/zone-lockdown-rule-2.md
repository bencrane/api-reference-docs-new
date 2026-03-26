# Get a Zone Lockdown rule

`GET /zones/{zone_id}/firewall/lockdowns/{lock_downs_id}`

Fetches the details of a Zone Lockdown rule.

## Parameters

- **lock_downs_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Response

### 200

Get a Zone Lockdown rule response

- **result** (object, optional): 

### 4XX

Get a Zone Lockdown rule response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
