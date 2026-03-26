# Get an Access application policy

`GET /accounts/{account_id}/access/apps/{app_id}/policies/{policy_id}`

Fetches a single Access policy configured for an application. Returns both exclusively owned and reusable policies used by the application.

## Parameters

- **app_id** (string, required) [path]: The application ID.
- **policy_id** (string, required) [path]: The policy ID.
- **account_id** (string, required) [path]: 

## Response

### 200

Get an Access policy response.

_Empty object_

### 4XX

Get an Access policy response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
