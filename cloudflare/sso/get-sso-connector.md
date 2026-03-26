# Get single SSO connector

`GET /accounts/{account_id}/sso_connectors/{sso_connector_id}`



## Parameters

- **account_id** (string, required) [path]: 
- **sso_connector_id** (string, required) [path]: 

## Response

### 200

Get SSO connector response

- **result** (object, optional): 

### 4XX

Get SSO connector response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
