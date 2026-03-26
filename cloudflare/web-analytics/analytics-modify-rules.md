# Update Web Analytics rules

`POST /accounts/{account_id}/rum/v2/{ruleset_id}/rules`

Modifies one or more rules in a Web Analytics ruleset with a single request.

## Parameters

- **account_id** (string, required) [path]: 
- **ruleset_id** (string, required) [path]: 

## Request Body

- **delete_rules** (array, optional): A list of rule identifiers to delete.
- **rules** (array, optional): A list of rules to create or update.

## Response

### 200

List of modified Web Analytics rules.

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
