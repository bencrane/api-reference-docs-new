# Restart Validation or Update Advanced Certificate Manager Certificate Pack

`PATCH /zones/{zone_id}/ssl/certificate_packs/{certificate_pack_id}`

For a given zone, restart validation or add cloudflare branding for an advanced certificate pack.  The former is only a validation operation for a Certificate Pack in a validation_timed_out status.

## Parameters

- **certificate_pack_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Request Body

- **cloudflare_branding** (boolean, optional): Whether or not to add Cloudflare Branding for the order.  This will add a subdomain of sni.cloudflaressl.com as the Common Name if set to true.

## Response

### 200

Restart Validation for Advanced Certificate Manager Certificate Pack response

- **result** (object, optional): A certificate pack with all its properties.

### 4XX

Restart Validation for Advanced Certificate Manager Certificate Pack response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
