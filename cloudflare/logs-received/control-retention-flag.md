# Get log retention flag

`GET /zones/{zone_id}/logs/control/retention/flag`

Gets log retention flag for Logpull API.

## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 200

Get log retention flag response

- **result** (object, optional): 

### 4XX

Get log retention flag response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
