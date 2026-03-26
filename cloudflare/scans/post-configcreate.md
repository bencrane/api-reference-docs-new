# Create a new Scan Config

`POST /accounts/{account_id}/cloudforce-one/scans/config`



## Parameters

- **account_id** (string, required) [path]: Defines the Account ID.

## Request Body

- **frequency** (number, optional): Defines the number of days between each scan (0 = One-off scan).
- **ips** (array, required): Defines a list of IP addresses or CIDR blocks to scan. The maximum number of total IP addresses allowed is 5000.
- **ports** (array, optional): Defines a list of ports to scan. Valid values are:"default", "all", or a comma-separated list of ports or range of ports (e.g. ["1-80", "443"]). "default" scans the 100 most commonly open ports.

## Response

### 200

Returns the created config.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Create a new Scan Config failure.

- **errors** (object, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional):
