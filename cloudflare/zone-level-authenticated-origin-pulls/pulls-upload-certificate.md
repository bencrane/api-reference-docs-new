# Upload Certificate

`POST /zones/{zone_id}/origin_tls_client_auth`

Upload your own certificate you want Cloudflare to use for edge-to-origin communication to override the shared certificate. Please note that it is important to keep only one certificate active. Also, make sure to enable zone-level authenticated origin pulls by making a PUT call to settings endpoint to see the uploaded certificate in use.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **certificate** (string, required): The zone's leaf certificate.
- **private_key** (string, required): The zone's private key.

## Response

### 200

Upload Certificate response

- **result** (object, optional): 

### 4XX

Upload Certificate response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
