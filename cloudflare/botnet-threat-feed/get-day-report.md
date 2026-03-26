# Get daily report

`GET /accounts/{account_id}/botnet_feed/asn/{asn_id}/day_report`

Gets all the data the botnet tracking database has for a given ASN registered to user account for given date. If no date is given, it will return results for the previous day.

## Parameters

- **account_id** (string, required) [path]: 
- **asn_id** (string, required) [path]: 
- **date** (string, optional) [query]: 

## Response

### 200

Get botnet feed report for day

_Empty object_

### 4XX

Get botnet feed report for day response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
