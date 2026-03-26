# Get certificate authority details

`GET /radar/ct/authorities/{ca_slug}`

Retrieves the requested CA information.

## Parameters

- **ca_slug** (string, required) [path]: Certificate authority SHA256 fingerprint.
- **format** (string, optional) [query]: Format in which results will be returned.

## Response

### 200

Successful response.

- **result** (object): 
- **success** (boolean): 

### 404

Not found.

- **error** (string):
