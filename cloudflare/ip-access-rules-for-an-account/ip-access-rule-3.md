# Update an IP Access rule

`PATCH /accounts/{account_id}/firewall/access_rules/rules/{rule_id}`

Updates an IP Access rule defined at the account level.

Note: This operation will affect all zones in the account.

## Parameters

- **rule_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

_Empty object_

## Response

### 200

Update an IP Access rule response.

- **result** (object, optional): 

### 4XX

Update an IP Access rule response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
