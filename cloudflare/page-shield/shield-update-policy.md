# Update a Page Shield policy

`PUT /zones/{zone_id}/page_shield/policies/{policy_id}`

Update a Page Shield policy by ID.

## Parameters

- **zone_id** (string, required) [path]: 
- **policy_id** (string, required) [path]: 

## Request Body

- **action** (string, optional): The action to take if the expression matches Values: `allow`, `log`, `add_reporting_directives`
- **description** (string, optional): A description for the policy
- **enabled** (boolean, optional): Whether the policy is enabled
- **expression** (string, optional): The expression which must match for the policy to be applied, using the Cloudflare Firewall rule expression syntax
- **value** (string, optional): The policy which will be applied

## Response

### 200

Update a Page Shield policy response

- **result** (object, optional): 

### 4XX

Update a Page Shield policy response failure

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful
