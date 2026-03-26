# Get `PhishGuard` reports

`GET /accounts/{account_id}/email-security/phishguard/reports`

Retrieves `PhishGuard` reports showing phishing attempts and suspicious email patterns
detected.

## Parameters

- **account_id** (string, required) [path]: 
- **from_date** (string, optional) [query]: 
- **to_date** (string, optional) [query]: 
- **start** (string, optional) [query]: The beginning of the search date range (RFC3339 format).
- **end** (string, optional) [query]: The end of the search date range (RFC3339 format).

## Response

### 200

Contains a list of PhishGuard reports.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): 
- **result** (array, optional): 

### 4XX

Client Error

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean):
