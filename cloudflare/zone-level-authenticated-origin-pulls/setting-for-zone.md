# Get Enablement Setting for Zone

`GET /zones/{zone_id}/origin_tls_client_auth/settings`

Get whether zone-level authenticated origin pulls is enabled or not. It is false by default.

## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 200

Get Enablement Setting for Zone response

- **result** (object, optional): 

### 4XX

Get Enablement Setting for Zone response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
