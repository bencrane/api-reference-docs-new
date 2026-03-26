# Get IP address details

`GET /radar/entities/ip`

Retrieves IP address information.

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
