# DNSSEC Details

`GET /zones/{zone_id}/dnssec`

Details about DNSSEC status and configuration.

## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 200

DNSSEC Details response.

- **result** (object, optional): 

### 4XX

DNSSEC Details response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
