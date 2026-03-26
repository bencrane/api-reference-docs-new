# Get an email scanner rule

`GET /accounts/{account_id}/dlp/email/rules/{rule_id}`

Gets detailed configuration for a specific DLP email scanning rule, including detection patterns and actions.

## Parameters

- **account_id** (string, required) [path]: 
- **rule_id** (string, required) [path]: 

## Response

### 200

Get Email Scanner Rule response.

- **result** (object, optional): 

### 4XX

Get Email Scanner Rule failure response.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
