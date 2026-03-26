# Get Automatic SSL/TLS enrollment status for the given zone

`GET /zones/{zone_id}/settings/ssl_automatic_mode`

If the system is enabled, the response will include next_scheduled_scan, representing the next time this zone will be scanned and the zone's ssl/tls encryption mode is potentially upgraded by the system. If the system is disabled, next_scheduled_scan will not be present in the response body.

## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 200

Get Automatic SSL/TLS Enrollment status response.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): Indicates the API call's success or failure.

### 4XX

Get Automatic SSL/TLS Enrollment status failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Indicates the API call's success or failure.
