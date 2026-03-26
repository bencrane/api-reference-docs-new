# Get account profile

`GET /accounts/{account_id}/profile`

Retrieves the profile information for a specific Cloudflare account, including organization details, settings, and metadata. This endpoint is commonly used to verify account access and retrieve account-level configuration.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

The request has succeeded.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): 

### 4XX

An unexpected error response.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean):
