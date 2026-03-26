# List Hyperdrives

`GET /accounts/{account_id}/hyperdrive/configs`

Returns a list of Hyperdrives.

## Parameters

- **account_id** (string, required) [path]: The Cloudflare account ID.

## Response

### 200

List Hyperdrives Response.

- **result** (array, optional): 

### 4XX

List Hyperdrives Failure Response.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Return the status of the API call success.
