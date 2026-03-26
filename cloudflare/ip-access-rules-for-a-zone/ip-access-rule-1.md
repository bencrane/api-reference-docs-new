# Delete an IP Access rule

`DELETE /zones/{zone_id}/firewall/access_rules/rules/{rule_id}`

Deletes an IP Access rule defined at the zone level.

Optionally, you can use the `cascade` property to specify that you wish to delete similar rules in other zones managed by the same zone owner.

## Parameters

- **zone_id** (string, required) [path]: 
- **rule_id** (string, required) [path]: 

## Request Body

- **cascade** (string, optional): The level to attempt to delete similar rules defined for other zones with the same owner. The default value is `none`, which will only delete the current rule. Using `basic` will delete rules that match the same action (mode) and configuration, while using `aggressive` will delete rules that match the same configuration. Values: `none`, `basic`, `aggressive`

## Response

### 200

Delete an IP Access rule response.

- **result** (object, optional): 

### 4XX

Delete an IP Access rule response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
