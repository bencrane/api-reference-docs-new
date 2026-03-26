# Create a Page Shield policy

`POST /zones/{zone_id}/page_shield/policies`

Create a Page Shield policy.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **action** (string, required): The action to take if the expression matches Values: `allow`, `log`, `add_reporting_directives`
- **description** (string, required): A description for the policy
- **enabled** (boolean, required): Whether the policy is enabled
- **expression** (string, required): The expression which must match for the policy to be applied, using the Cloudflare Firewall rule expression syntax
- **value** (string, required): The policy which will be applied

## Response

### 200

Create a Page Shield policy response

- **result** (object, optional): 

### 4XX

Create a Page Shield policy response failure

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful
