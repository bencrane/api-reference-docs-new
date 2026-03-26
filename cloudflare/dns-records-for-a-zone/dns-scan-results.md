# Review Scanned DNS Records

`POST /zones/{zone_id}/dns_records/scan/review`

Accept or reject DNS records found by the DNS records scan. Accepted records will be permanently added to the zone, while rejected records will be permanently deleted.


## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **accepts** (array, optional): 
- **rejects** (array, optional): 

## Response

### 200

Records reviewed successfully

_Empty object_

### 4XX

Review failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
