# Delete a Zone Lockdown rule

`DELETE /zones/{zone_id}/firewall/lockdowns/{lock_downs_id}`

Deletes an existing Zone Lockdown rule.

## Parameters

- **lock_downs_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 


## Response

### 200

Delete a Zone Lockdown rule response

- **result** (object): 

### 4XX

Delete a Zone Lockdown rule response failure

- **result** (object, optional):  Values: ``
- **errors** (object, optional): 
- **messages** (object, optional): 
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
