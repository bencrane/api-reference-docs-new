# Get variants setting

`GET /zones/{zone_id}/cache/variants`

Variant support enables caching variants of images with certain file extensions in addition to the original. This only applies when the origin server sends the 'Vary: Accept' response header. If the origin server sends 'Vary: Accept' but does not serve the variant requested, the response will not be cached. This will be indicated with BYPASS cache status in the response headers.

## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 200

Get variants setting response.

_Empty object_

### 4XX

Get variants setting response failure.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
