# Get a zone token validation rule

`GET /zones/{zone_id}/token_validation/rules/{rule_id}`

Get a zone token validation rule.

## Response

### 200

OK

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): A Token Validation rule that can enforce security policies using JWT Tokens.

### 4XX

Failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
