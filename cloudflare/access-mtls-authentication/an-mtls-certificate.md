# Add an mTLS certificate

`POST /accounts/{account_id}/access/certificates`

Adds a new mTLS root certificate to Access.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **associated_hostnames** (array, optional): The hostnames of the applications that will use this certificate.
- **certificate** (string, required): The certificate content.
- **name** (string, required): The name of the certificate.

## Response

### 201

Add an mTLS certificate response

_Empty object_

### 4XX

Add an mTLS certificate response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
