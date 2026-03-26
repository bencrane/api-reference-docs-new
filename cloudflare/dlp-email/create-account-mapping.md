# Create mapping

`POST /accounts/{account_id}/dlp/email/account_mapping`

Creates a mapping between a Cloudflare account and an email provider for DLP email scanning integration.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **auth_requirements** (object, required): 

## Response

### 200

New Email Scanner Account Mapping response.

- **result** (object, optional): 

### 4XX

New Email Scanner Account Mapping failure response.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
