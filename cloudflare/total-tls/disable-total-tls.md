# Enable or Disable Total TLS

`POST /zones/{zone_id}/acm/total_tls`

Set Total TLS Settings or disable the feature for a Zone.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **certificate_authority** (string, optional): The Certificate Authority that Total TLS certificates will be issued through. Values: `google`, `lets_encrypt`, `ssl_com`
- **enabled** (boolean, required): If enabled, Total TLS will order a hostname specific TLS certificate for any proxied A, AAAA, or CNAME record in your zone.

## Response

### 200

Enable or Disable Total TLS response

- **result** (object, optional): 

### 4XX

Enable or Disable Total TLS response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
