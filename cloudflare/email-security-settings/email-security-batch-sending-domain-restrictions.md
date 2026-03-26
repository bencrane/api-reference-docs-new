# Batch Sending Domain Restrictions

`POST /accounts/{account_id}/email-security/settings/sending_domain_restrictions/batch`

Send a Batch of `sending_domain_restrictions` API calls to be executed together.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **deletes** (array, required): 

## Response

### 200



- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): 
- **result** (object, optional): 

### 4XX

Client Error

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean):
