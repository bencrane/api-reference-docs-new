# Create a service token

`POST /accounts/{account_id}/access/service_tokens`

Generates a new service token. **Note:** This is the only time you can get the Client Secret. If you lose the Client Secret, you will have to rotate the Client Secret or create a new service token.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **client_secret_version** (number, optional): A version number identifying the current `client_secret` associated with the service token. Incrementing it triggers a rotation; the previous secret will still be accepted until the time indicated by `previous_client_secret_expires_at`.
- **duration** (string, optional): The duration for how long the service token will be valid. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h. The default is 1 year in hours (8760h).
- **name** (string, required): The name of the service token.
- **previous_client_secret_expires_at** (string, optional): The expiration of the previous `client_secret`. This can be modified at any point after a rotation. For example, you may extend it further into the future if you need more time to update services with the new secret; or move it into the past to immediately invalidate the previous token in case of compromise.

## Response

### 201

Create a service token response

_Empty object_

### 4XX

Create a service token response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
