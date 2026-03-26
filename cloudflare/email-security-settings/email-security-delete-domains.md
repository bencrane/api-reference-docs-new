# Unprotect multiple email domains

`DELETE /accounts/{account_id}/email-security/settings/domains`

Bulk removes multiple domains from email security configuration in a single request.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

Array of object

## Response

### 200



- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): 
- **result** (array, optional): 

### 4XX

Client Error

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean):
