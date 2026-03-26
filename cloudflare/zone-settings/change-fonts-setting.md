# Change Cloudflare Fonts setting

`PATCH /zones/{zone_id}/settings/fonts`

Enhance your website's font delivery with Cloudflare Fonts. Deliver Google Hosted fonts from your own domain,
boost performance, and enhance user privacy. Refer to the Cloudflare Fonts documentation for more information.


## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **value** (string, required): Whether the feature is enabled or disabled. Values: `on`, `off`

## Response

### 200

Change Cloudflare Fonts setting response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful.
- **result** (object, optional): Enhance your website's font delivery with Cloudflare Fonts. Deliver Google Hosted fonts from your own domain,
boost performance, and enhance user privacy. Refer to the Cloudflare Fonts documentation for more information.


### 4XX

Change Cloudflare Fonts setting response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
