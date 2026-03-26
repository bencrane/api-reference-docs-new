# Begin SSO connector verification

`POST /accounts/{account_id}/sso_connectors/{sso_connector_id}/begin_verification`



## Parameters

- **account_id** (string, required) [path]: 
- **sso_connector_id** (string, required) [path]: 

## Response

### 200

Begin SSO connector verification process response

_Empty object_

### 4XX

Begin SSO connector verification process response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
