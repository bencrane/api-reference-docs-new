# Get URL Normalization settings

`GET /zones/{zone_id}/url_normalization`

Fetches the current URL Normalization settings.

## Parameters

- **zone_id** (string, required) [path]: 

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
