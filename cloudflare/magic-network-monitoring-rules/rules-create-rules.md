# Create rules

`POST /accounts/{account_id}/mnm/rules`

Create network monitoring rules for account. Currently only supports creating a single rule per API request.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **automatic_advertisement** (boolean, optional): Toggle on if you would like Cloudflare to automatically advertise the IP Prefixes within the rule via Magic Transit when the rule is triggered. Only available for users of Magic Transit.
- **bandwidth** (number, optional): The number of bits per second for the rule. When this value is exceeded for the set duration, an alert notification is sent. Minimum of 1 and no maximum.
- **duration** (string, required): The amount of time that the rule threshold must be exceeded to send an alert notification. The final value must be equivalent to one of the following 8 values ["1m","5m","10m","15m","20m","30m","45m","60m"]. Values: `1m`, `5m`, `10m`, `15m`, `20m`, `30m`, `45m`, `60m`
- **name** (string, required): The name of the rule. Must be unique. Supports characters A-Z, a-z, 0-9, underscore (_), dash (-), period (.), and tilde (~). You can’t have a space in the rule name. Max 256 characters.
- **packet_threshold** (number, optional): The number of packets per second for the rule. When this value is exceeded for the set duration, an alert notification is sent. Minimum of 1 and no maximum.
- **prefixes** (array, optional): 

## Response

### 200

Create rules response

- **result** (object, optional): 

### 4XX

Create rules response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
