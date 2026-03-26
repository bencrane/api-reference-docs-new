# Get Zero Trust certificate configuration

`GET /accounts/{account_id}/gateway/configuration/custom_certificate`

> **Deprecated**

Retrieve the current Zero Trust certificate configuration.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

Zero Trust account configuration response.

- **binding_status** (string): Indicate the internal certificate status.
- **enabled** (boolean): Specify whether to enable a custom certificate authority for signing Gateway traffic.
- **id** (string): Specify the UUID of the certificate (ID from MTLS certificate store).
- **updated_at** (string): 

### 4XX

Zero Trust account configuration response failure.

- **binding_status** (string, optional): Indicate the internal certificate status.
- **enabled** (boolean, optional): Specify whether to enable a custom certificate authority for signing Gateway traffic.
- **id** (string, optional): Specify the UUID of the certificate (ID from MTLS certificate store).
- **updated_at** (string, optional): 
- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Indicate whether the API call was successful. Values: `false`
