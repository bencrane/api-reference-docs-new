# Get list of ASNs

`GET /accounts/{account_id}/botnet_feed/configs/asn`

Gets a list of all ASNs registered for a user for the DDoS Botnet Feed API.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

Get list of ASNs response

_Empty object_

### 4XX

Get list of ASNs response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
