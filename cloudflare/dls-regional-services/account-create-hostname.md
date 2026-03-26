# Create Regional Hostname

`POST /zones/{zone_id}/addressing/regional_hostnames`

Create a new Regional Hostname entry. Cloudflare will only use data centers that are physically located within the chosen region to decrypt and service HTTPS traffic. Learn more about [Regional Services](https://developers.cloudflare.com/data-localization/regional-services/get-started/).

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **hostname** (string, required): DNS hostname to be regionalized, must be a subdomain of the zone. Wildcards are supported for one level, e.g `*.example.com`
- **region_key** (string, required): Identifying key for the region
- **routing** (string, optional): Configure which routing method to use for the regional hostname

## Response

### 200

Create hostname response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Failure to create hostname

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
