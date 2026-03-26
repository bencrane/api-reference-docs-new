# Update a Zone Lockdown rule

`PUT /zones/{zone_id}/firewall/lockdowns/{lock_downs_id}`

Updates an existing Zone Lockdown rule.

## Parameters

- **lock_downs_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Request Body

- **configurations** (array, required): A list of IP addresses or CIDR ranges that will be allowed to access the URLs specified in the Zone Lockdown rule. You can include any number of `ip` or `ip_range` configurations.
- **urls** (array, required): The URLs to include in the current WAF override. You can use wildcards. Each entered URL will be escaped before use, which means you can only use simple wildcard patterns.

## Response

### 200

Update a Zone Lockdown rule response

- **result** (object, optional): 

### 4XX

Update a Zone Lockdown rule response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
