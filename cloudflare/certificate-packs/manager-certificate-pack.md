# Order Advanced Certificate Manager Certificate Pack

`POST /zones/{zone_id}/ssl/certificate_packs/order`

For a given zone, order an advanced certificate pack.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **certificate_authority** (string, required): Certificate Authority selected for the order.  For information on any certificate authority specific details or restrictions [see this page for more details.](https://developers.cloudflare.com/ssl/reference/certificate-authorities) Values: `google`, `lets_encrypt`, `ssl_com`
- **cloudflare_branding** (boolean, optional): Whether or not to add Cloudflare Branding for the order.  This will add a subdomain of sni.cloudflaressl.com as the Common Name if set to true.
- **hosts** (array, required): Comma separated list of valid host names for the certificate packs. Must contain the zone apex, may not contain more than 50 hosts, and may not be empty.
- **type** (string, required): Type of certificate pack. Values: `advanced`
- **validation_method** (string, required): Validation Method selected for the order. Values: `txt`, `http`, `email`
- **validity_days** (integer, required): Validity Days selected for the order. Values: `14`, `30`, `90`, `365`

## Response

### 200

Order Advanced Certificate Manager Certificate Pack response

- **result** (object, optional): A certificate pack with all its properties.

### 4XX

Order Advanced Certificate Manager Certificate Pack response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
