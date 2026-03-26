# Get device (deprecated)

`GET /accounts/{account_id}/devices/{device_id}`

> **Deprecated**

Fetches a single WARP device. Not supported when [multi-user mode](https://developers.cloudflare.com/cloudflare-one/connections/connect-devices/warp/deployment/mdm-deployment/windows-multiuser/) is enabled for the account.

**Deprecated**: please use one of the following endpoints instead:
- GET /accounts/{account_id}/devices/physical-devices/{device_id}
- GET /accounts/{account_id}/devices/registrations/{registration_id}


## Parameters

- **device_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Get device details response.

- **result** (object, optional): 

### 4XX

Get device details response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
