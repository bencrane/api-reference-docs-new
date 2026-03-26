# Create a trusted email domain

`POST /accounts/{account_id}/email-security/settings/trusted_domains`

Adds a domain to the trusted domains list for email security, reducing false positive
detections.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

One of: object, array

## Response

### 201

Contains the new trusted domain in the shape of the request body.

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
