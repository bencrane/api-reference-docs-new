# Update log retention flag

`POST /zones/{zone_id}/logs/control/retention/flag`

Updates log retention flag for Logpull API.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **flag** (boolean, optional): The log retention flag for Logpull API.

## Response

### 200

Update log retention flag response

- **result** (object, optional): 

### 4XX

Update log retention flag response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
