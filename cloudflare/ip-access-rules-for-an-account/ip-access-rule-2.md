# Get an IP Access rule

`GET /accounts/{account_id}/firewall/access_rules/rules/{rule_id}`

Fetches the details of an IP Access rule defined at the account level.

## Parameters

- **rule_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Get an IP Access rule response.

- **result** (object, optional): 

### 4XX

Get an IP Access rule response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
