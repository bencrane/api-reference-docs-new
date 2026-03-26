# Update Hyperdrive

`PUT /accounts/{account_id}/hyperdrive/configs/{hyperdrive_id}`

Updates and returns the specified Hyperdrive configuration.

## Parameters

- **account_id** (string, required) [path]: The Cloudflare account ID.
- **hyperdrive_id** (string, required) [path]: The unique identifier of the Hyperdrive configuration.

## Request Body

- **caching** (object, optional): 
- **created_on** (string, optional): Defines the creation time of the Hyperdrive configuration.
- **id** (string, required): Define configurations using a unique string identifier.
- **modified_on** (string, optional): Defines the last modified time of the Hyperdrive configuration.
- **mtls** (object, optional): 
- **name** (string, required): The name of the Hyperdrive configuration. Used to identify the configuration in the Cloudflare dashboard and API.
- **origin** (object, required): 
- **origin_connection_limit** (integer, optional): The (soft) maximum number of connections the Hyperdrive is allowed to make to the origin database.

Maximum allowed: 20 for free tier accounts, 100 for paid tier accounts.
If not specified, defaults to 20 for free tier and 60 for paid tier.
Contact Cloudflare if you need a higher limit.


## Response

### 200

Update Hyperdrive Response.

- **result** (object, optional): 

### 4XX

Update Hyperdrive Failure Response.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Return the status of the API call success.
