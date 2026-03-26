# Get mapping

`GET /accounts/{account_id}/dlp/email/account_mapping`

Retrieves the email provider mapping configuration for DLP email scanning.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

Get Email Scanner Account Mapping response.

- **result** (object, optional): 

### 4XX

Get Email Scanner Account Mapping failure response.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
