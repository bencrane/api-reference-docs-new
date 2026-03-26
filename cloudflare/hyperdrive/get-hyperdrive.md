# Get Hyperdrive

`GET /accounts/{account_id}/hyperdrive/configs/{hyperdrive_id}`

Returns the specified Hyperdrive configuration.

## Parameters

- **account_id** (string, required) [path]: The Cloudflare account ID.
- **hyperdrive_id** (string, required) [path]: The unique identifier of the Hyperdrive configuration.

## Response

### 200

Get Hyperdrive Response.

- **result** (object, optional): 

### 4XX

Get Hyperdrive Failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Return the status of the API call success.
