# Get Multiple Domain Details

`GET /accounts/{account_id}/intel/domain/bulk`

Same as summary.

## Parameters

- **account_id** (string, required) [path]: 
- **domain** (array, optional) [query]: Accepts multiple values like `?domain=cloudflare.com&domain=example.com`.

## Response

### 200

Get Multiple Domain Details response.

_Empty object_

### 4XX

Get Multiple Domain Details response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful.
