# Batch Allow Policies

`POST /accounts/{account_id}/email-security/settings/allow_policies/batch`

Send a Batch of Allow Policies API calls to be executed together.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **deletes** (array, required): 
- **patches** (array, required): 
- **posts** (array, required): 
- **puts** (array, required): 

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
