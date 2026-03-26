# Update a DEX Rule

`PATCH /accounts/{account_id}/dex/rules/{rule_id}`

Update a DEX Rule

## Parameters

- **account_id** (string, required) [path]: unique identifier linked to an account in the API request path
- **rule_id** (string, required) [path]: unique identifier of the rule

## Request Body

- **description** (string, optional): 
- **match** (string, optional): The wirefilter expression to match.
- **name** (string, optional): The name of the Rule.

## Response

### 200

success response

- **result** (object, optional): 

### 4XX

Update DEX Rule failure response

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
