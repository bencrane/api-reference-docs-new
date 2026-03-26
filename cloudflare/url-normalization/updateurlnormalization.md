# Update URL Normalization settings

`PUT /zones/{zone_id}/url_normalization`

Updates the URL Normalization settings.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **scope** (string, required): The scope of the URL normalization. Values: `incoming`, `both`, `none`
- **type** (string, required): The type of URL normalization performed by Cloudflare. Values: `cloudflare`, `rfc3986`

## Response

### 200

A URL Normalization response.

- **errors** (enum, optional):  Values: ``
- **messages** (array, optional): A list of warning messages.
- **result** (object, optional): A URL Normalization object.
- **success** (enum, optional):  Values: `true`

### 4XX

A failure response.

- **errors** (array, optional): A list of error messages.
- **messages** (array, optional): A list of warning messages.
- **result** (enum, optional):  Values: ``
- **success** (enum, optional):  Values: `false`
