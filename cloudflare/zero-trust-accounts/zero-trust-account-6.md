# Update Zero Trust account logging settings

`PUT /accounts/{account_id}/gateway/logging`

Update logging settings for the current Zero Trust account.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **redact_pii** (boolean, optional): Indicate whether to redact personally identifiable information from activity logging (PII fields include source IP, user email, user ID, device ID, URL, referrer, and user agent).
- **settings_by_rule_type** (object, optional): Configure logging settings for each rule type.

## Response

### 200

Logging settings update response.

- **result** (object, optional): 

### 4XX

Logging settings update response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Indicate whether the API call was successful. Values: `false`
