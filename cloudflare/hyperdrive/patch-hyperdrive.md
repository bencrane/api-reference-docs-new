# Patch Hyperdrive

`PATCH /accounts/{account_id}/hyperdrive/configs/{hyperdrive_id}`

Patches and returns the specified Hyperdrive configuration. Custom caching settings are not kept if caching is disabled.

## Parameters

- **account_id** (string, required) [path]: The Cloudflare account ID.
- **hyperdrive_id** (string, required) [path]: The unique identifier of the Hyperdrive configuration.

## Request Body

- **caching** (object, optional): 
- **mtls** (object, optional): 
- **name** (string, optional): The name of the Hyperdrive configuration. Used to identify the configuration in the Cloudflare dashboard and API.
- **origin** (object, optional): 
- **origin_connection_limit** (integer, optional): The (soft) maximum number of connections the Hyperdrive is allowed to make to the origin database.

Maximum allowed: 20 for free tier accounts, 100 for paid tier accounts.
If not specified, defaults to 20 for free tier and 60 for paid tier.
Contact Cloudflare if you need a higher limit.


## Response

### 200

Patch Hyperdrive Response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): 
- **success** (boolean, optional): Return the status of the API call success. Values: `true`

### 4XX

Patch Hyperdrive Failure Response.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Return the status of the API call success.
