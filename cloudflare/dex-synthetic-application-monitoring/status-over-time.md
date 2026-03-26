# List fleet status aggregate details by dimension

`GET /accounts/{account_id}/dex/fleet-status/over-time`

List details for devices using WARP, up to 7 days

## Parameters

- **account_id** (string, required) [path]: Unique identifier for account
- **to** (string, required) [query]: Time range end in ISO format
- **from** (string, required) [query]: Time range beginning in ISO format
- **colo** (string, optional) [query]: Cloudflare colo
- **device_id** (string, optional) [query]: Device-specific ID, given as UUID v4

## Response

### 200

List DEX devices response

- **result** (object, optional): 

### 4XX

DEX HTTP test details failure response

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
