# List Signing Keys

`GET /accounts/{account_id}/images/v1/keys`

Lists your signing keys. These can be found on your Cloudflare Images dashboard.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

List Signing Keys response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `true`

### 4XX

List Signing Keys response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
