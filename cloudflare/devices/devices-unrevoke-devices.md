# Unrevoke devices (deprecated)

`POST /accounts/{account_id}/devices/unrevoke`

> **Deprecated**

Unrevokes a list of devices. Not supported when [multi-user mode](https://developers.cloudflare.com/cloudflare-one/connections/connect-devices/warp/deployment/mdm-deployment/windows-multiuser/) is enabled.

**Deprecated**: please use POST /accounts/{account_id}/devices/registrations/unrevoke instead.


## Parameters

- **account_id** (string, required) [path]: 

## Request Body

Array of string

## Response

### 200

Unrevoke devices response.

_Empty object_

### 4XX

Unrevoke devices response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
