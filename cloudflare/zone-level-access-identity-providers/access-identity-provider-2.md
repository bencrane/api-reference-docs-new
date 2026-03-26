# Get an Access identity provider

`GET /zones/{zone_id}/access/identity_providers/{identity_provider_id}`

Fetches a configured identity provider.

## Parameters

- **identity_provider_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Response

### 200

Get an Access identity provider response

_Empty object_

### 4XX

Get an Access identity provider response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
