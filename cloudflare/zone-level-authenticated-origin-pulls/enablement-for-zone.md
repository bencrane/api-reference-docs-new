# Set Enablement for Zone

`PUT /zones/{zone_id}/origin_tls_client_auth/settings`

Enable or disable zone-level authenticated origin pulls. 'enabled' should be set true either before/after the certificate is uploaded to see the certificate in use.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **enabled** (boolean, required): Indicates whether zone-level authenticated origin pulls is enabled.

## Response

### 200

Set Enablement for Zone response

- **result** (object, optional): 

### 4XX

Set Enablement for Zone response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
