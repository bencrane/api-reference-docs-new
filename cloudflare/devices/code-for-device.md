# Get override codes (deprecated)


`GET /accounts/{account_id}/devices/{device_id}/override_codes`

> **Deprecated**

Fetches a one-time use admin override code for a device. This relies on the **Admin Override** setting being enabled in your device configuration. Not supported when [multi-user mode](https://developers.cloudflare.com/cloudflare-one/connections/connect-devices/warp/deployment/mdm-deployment/windows-multiuser/) is enabled for the account.
**Deprecated:** please use GET /accounts/{account_id}/devices/registrations/{registration_id}/override_codes instead.


## Parameters

- **device_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Get an admin override code for a device response.

- **result** (object, optional): 

### 4XX

Get an admin override code for a device response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
