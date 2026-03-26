# List apps

`GET /accounts/{account_id}/calls/apps`

Lists all apps in the Cloudflare account

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

List apps response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (array, optional): 

### 4XX

List apps response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
