# Get DEX Rule

`GET /accounts/{account_id}/dex/rules/{rule_id}`

Get details for a DEX Rule

## Parameters

- **account_id** (string, required) [path]: unique identifier linked to an account in the API request path
- **rule_id** (string, required) [path]: unique identifier of the rule

## Response

### 200

success response

- **result** (object, optional): 

### 4XX

List DEX Rule failure response

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
