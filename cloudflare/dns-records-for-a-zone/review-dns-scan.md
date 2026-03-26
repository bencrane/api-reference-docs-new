# List Scanned DNS Records

`GET /zones/{zone_id}/dns_records/scan/review`

Retrieves the list of DNS records discovered up to this point by the asynchronous scan. These records are temporary until explicitly accepted or rejected via `POST /scan/review`. Additional records may be discovered by the scan later.


## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 200

List of discovered DNS records

_Empty object_

### 4XX

Scan review failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
