# Update a service token

`PUT /zones/{zone_id}/access/service_tokens/{service_token_id}`

Updates a configured service token.

## Parameters

- **service_token_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Request Body

- **client_secret_version** (number, optional): A version number identifying the current `client_secret` associated with the service token. Incrementing it triggers a rotation; the previous secret will still be accepted until the time indicated by `previous_client_secret_expires_at`.
- **duration** (string, optional): The duration for how long the service token will be valid. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h. The default is 1 year in hours (8760h).
- **name** (string, optional): The name of the service token.
- **previous_client_secret_expires_at** (string, optional): The expiration of the previous `client_secret`. This can be modified at any point after a rotation. For example, you may extend it further into the future if you need more time to update services with the new secret; or move it into the past to immediately invalidate the previous token in case of compromise.

## Response

### 200

Update a service token response

_Empty object_

### 4XX

Update a service token response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
