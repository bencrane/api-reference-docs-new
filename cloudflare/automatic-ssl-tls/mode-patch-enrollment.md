# Patch Automatic SSL/TLS Enrollment status for given zone

`PATCH /zones/{zone_id}/settings/ssl_automatic_mode`

The automatic system is enabled when this endpoint is hit with value in the request body is set to "auto", and disabled when the request body value is set to "custom".

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **value** (string, required): Controls enablement of Automatic SSL/TLS. Values: `auto`, `custom`

## Response

### 200

Patch Automatic SSL/TLS Enrollment status response.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): Indicates the API call's success or failure.

### 4XX

Patch Automatic SSL/TLS Enrollment status failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Indicates the API call's success or failure.
