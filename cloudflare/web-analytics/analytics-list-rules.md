# List rules in Web Analytics ruleset

`GET /accounts/{account_id}/rum/v2/{ruleset_id}/rules`

Lists all the rules in a Web Analytics ruleset.

## Parameters

- **account_id** (string, required) [path]: 
- **ruleset_id** (string, required) [path]: 

## Response

### 200

List of Web Analytics rules in the ruleset.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful.
- **result** (object, optional): 

### 4XX

Failure response.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
