# Fetch limits associated with DLP for account

`GET /accounts/{account_id}/dlp/limits`

Retrieves current DLP usage limits and quotas for the account, including dataset limits and scan quotas.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

Limits retrieved successfully.

- **result** (object, optional): 

### 4XX

Limits get failed.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
