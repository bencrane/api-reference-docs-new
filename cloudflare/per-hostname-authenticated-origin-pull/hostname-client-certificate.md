# Upload a Hostname Client Certificate

`POST /zones/{zone_id}/origin_tls_client_auth/hostnames/certificates`

Upload a certificate to be used for client authentication on a hostname. 10 hostname certificates per zone are allowed.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **certificate** (string, required): The hostname certificate.
- **private_key** (string, required): The hostname certificate's private key.

## Response

### 200

Upload a Hostname Client Certificate response

- **result** (object, optional): 

### 4XX

Upload a Hostname Client Certificate response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
