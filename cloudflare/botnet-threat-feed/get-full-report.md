# Get full report

`GET /accounts/{account_id}/botnet_feed/asn/{asn_id}/full_report`

Gets all the data the botnet threat feed tracking database has for a given ASN registered to user account.

## Parameters

- **account_id** (string, required) [path]: 
- **asn_id** (string, required) [path]: 

## Response

### 200

Get full botnet feed report

_Empty object_

### 4XX

Get full botnet feed report response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
