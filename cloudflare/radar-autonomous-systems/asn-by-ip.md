# Get AS details by IP address

`GET /radar/entities/asns/ip`

Retrieves the requested autonomous system information based on IP address. Population estimates come from APNIC (refer to https://labs.apnic.net/?p=526).

## Parameters

- **ip** (string, required) [query]: IP address.
- **format** (string, optional) [query]: Format in which results will be returned.

## Response

### 200

Successful response.

- **result** (object): 
- **success** (boolean): 

### 404

Not found.

- **error** (string):
