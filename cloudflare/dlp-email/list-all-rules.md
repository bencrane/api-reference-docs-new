# List all email scanner rules

`GET /accounts/{account_id}/dlp/email/rules`

Lists all email scanner rules for an account.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

List all email scanner rules response.

- **result** (array, optional): 

### 4XX

List all email scanner rules failure response.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
