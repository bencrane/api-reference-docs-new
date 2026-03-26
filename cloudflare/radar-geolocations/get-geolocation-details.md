# Get Geolocation details

`GET /radar/geolocations/{geo_id}`

Retrieves the requested Geolocation information. Geolocation names can be localized by sending an `Accept-Language` HTTP header with a BCP 47 language tag (e.g., `Accept-Language: pt-PT`). The full quality-value chain is supported (e.g., `pt-PT,pt;q=0.9,en;q=0.8`).

## Parameters

- **geo_id** (string, required) [path]: Geolocation ID. Refer to [GeoNames](https://download.geonames.org/export/dump/readme.txt)
- **format** (string, optional) [query]: Format in which results will be returned.

## Response

### 200

Successful response.

- **result** (object): 
- **success** (boolean): 

### 404

Not found.

- **error** (string):
