# Delete an ASN

`DELETE /accounts/{account_id}/botnet_feed/configs/asn/{asn_id}`

Delete an ASN from botnet threat feed for a given user.

## Parameters

- **account_id** (string, required) [path]: 
- **asn_id** (string, required) [path]: 

## Response

### 200

Delete ASN response

_Empty object_

### 4XX

Delete ASN response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
