# List devices (deprecated)

`GET /accounts/{account_id}/devices`

> **Deprecated**

List WARP devices. Not supported when [multi-user mode](https://developers.cloudflare.com/cloudflare-one/connections/connect-devices/warp/deployment/mdm-deployment/windows-multiuser/) is enabled for the account.

**Deprecated**: please use one of the following endpoints instead:
- GET /accounts/{account_id}/devices/physical-devices
- GET /accounts/{account_id}/devices/registrations


## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

List devices response.

- **result** (array, optional): 

### 4XX

List devices response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
