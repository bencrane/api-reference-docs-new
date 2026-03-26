# Update an mTLS certificate

`PUT /zones/{zone_id}/access/certificates/{certificate_id}`

Updates a configured mTLS certificate.

## Parameters

- **certificate_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Request Body

- **associated_hostnames** (array, required): The hostnames of the applications that will use this certificate.
- **name** (string, optional): The name of the certificate.

## Response

### 200

Update an mTLS certificate response

_Empty object_

### 4XX

Update an mTLS certificate response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
