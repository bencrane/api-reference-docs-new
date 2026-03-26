# Get WHOIS Record

`GET /accounts/{account_id}/intel/whois`

Retrieves WHOIS registration data for a domain, including registrant and nameserver information.

## Parameters

- **account_id** (string, required) [path]: 
- **domain** (string, optional) [query]: 

## Response

### 200

Get WHOIS Record response.

- **result** (object, optional): 

### 4XX

Get WHOIS Record response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Returns a boolean for the success/failure of the API call. Values: `false`
