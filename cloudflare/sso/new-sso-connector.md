# Initialize new SSO connector

`POST /accounts/{account_id}/sso_connectors`



## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **begin_verification** (boolean, optional): Begin the verification process after creation
- **email_domain** (string, required): Email domain of the new SSO connector
- **use_fedramp_language** (boolean, optional): Controls the display of FedRAMP language to the user during SSO login

## Response

### 200

Initialize new SSO connector response

- **result** (object, optional): 

### 4XX

Initialize new SSO connector response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
