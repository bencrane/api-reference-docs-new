# Get ASN Overview.

`GET /accounts/{account_id}/intel/asn/{asn}`

Gets an overview of the Autonomous System Number (ASN) and a list of subnets for it.

## Parameters

- **asn** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Get ASN Overview response.

_Empty object_

### 4XX

Get ASN Overview response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful.
