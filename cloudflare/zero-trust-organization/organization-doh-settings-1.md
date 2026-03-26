# Update your Zero Trust organization DoH settings

`PUT /accounts/{account_id}/access/organizations/doh`

Updates the DoH settings for your Zero Trust organization.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **doh_jwt_duration** (string, optional): The duration the DoH JWT is valid for. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h.  Note that the maximum duration for this setting is the same as the key rotation period on the account. Default expiration is 24h
- **service_token_id** (string, optional): The uuid of the service token you want to use for DoH authentication

## Response

### 201

Update your Zero Trust organization DoH settings response

- **result** (object, optional): 

### 4XX

Update your Zero Trust organization DoH settings response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
