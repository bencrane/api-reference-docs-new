# Rotate a service token

`POST /accounts/{account_id}/access/service_tokens/{service_token_id}/rotate`

Generates a new Client Secret for a service token and revokes the old one.

## Parameters

- **service_token_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

- **previous_client_secret_expires_at** (string, optional): The expiration of the previous `client_secret`. If not provided, it defaults to the current timestamp in order to immediately expire the previous secret.

## Response

### 200

Rotate a service token response

_Empty object_

### 4XX

Rotate a service token response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
