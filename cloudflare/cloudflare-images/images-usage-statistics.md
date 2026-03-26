# Images usage statistics

`GET /accounts/{account_id}/images/v1/stats`

Fetch image statistics details for Cloudflare Images. The returned statistics detail storage usage, including the current image count vs this account's allowance.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

Images usage statistics response

- **result** (object, optional): 

### 4XX

Images usage statistics response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
