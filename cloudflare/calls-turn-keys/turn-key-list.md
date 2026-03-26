# List TURN Keys

`GET /accounts/{account_id}/calls/turn_keys`

Lists all TURN keys in the Cloudflare account

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

List TURN key response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (array, optional): 

### 4XX

List TURN key response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
