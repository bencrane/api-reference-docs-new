# Update SSO connector state

`PATCH /accounts/{account_id}/sso_connectors/{sso_connector_id}`



## Parameters

- **account_id** (string, required) [path]: 
- **sso_connector_id** (string, required) [path]: 

## Request Body

- **enabled** (boolean, optional): SSO Connector enabled state
- **use_fedramp_language** (boolean, optional): Controls the display of FedRAMP language to the user during SSO login

## Response

### 200

Update SSO connector state response

- **result** (object, optional): 

### 4XX

Update SSO connector state response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
