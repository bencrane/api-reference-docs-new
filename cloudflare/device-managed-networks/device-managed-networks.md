# List your device managed networks

`GET /accounts/{account_id}/devices/networks`

Fetches a list of managed networks for an account.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

List your device managed networks response.

- **result** (array, optional): 

### 4XX

List your device managed networks response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
