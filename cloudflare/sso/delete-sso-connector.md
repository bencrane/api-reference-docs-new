# Delete SSO connector

`DELETE /accounts/{account_id}/sso_connectors/{sso_connector_id}`



## Parameters

- **account_id** (string, required) [path]: 
- **sso_connector_id** (string, required) [path]: 

## Response

### 200

Delete SSO connector response

_Empty object_

### 4XX

Delete SSO connector response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
