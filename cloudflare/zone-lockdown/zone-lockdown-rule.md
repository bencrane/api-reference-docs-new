# Create a Zone Lockdown rule

`POST /zones/{zone_id}/firewall/lockdowns`

Creates a new Zone Lockdown rule.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **configurations** (array, required): A list of IP addresses or CIDR ranges that will be allowed to access the URLs specified in the Zone Lockdown rule. You can include any number of `ip` or `ip_range` configurations.
- **description** (string, optional): An informative summary of the rule. This value is sanitized and any tags will be removed.
- **paused** (boolean, optional): When true, indicates that the rule is currently paused.
- **priority** (number, optional): The priority of the rule to control the processing order. A lower number indicates higher priority. If not provided, any rules with a configured priority will be processed before rules without a priority.
- **urls** (array, required): The URLs to include in the current WAF override. You can use wildcards. Each entered URL will be escaped before use, which means you can only use simple wildcard patterns.

## Response

### 200

Create a Zone Lockdown rule response

- **result** (object, optional): 

### 4XX

Create a Zone Lockdown rule response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
