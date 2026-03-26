# Create Health Check

`POST /zones/{zone_id}/smart_shield/healthchecks`

Create a new health check.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **address** (string, required): The hostname or IP address of the origin server to run health checks on.
- **check_regions** (array, optional): A list of regions from which to run health checks. Null means Cloudflare will pick a default region.
- **consecutive_fails** (integer, optional): The number of consecutive fails required from a health check before changing the health to unhealthy.
- **consecutive_successes** (integer, optional): The number of consecutive successes required from a health check before changing the health to healthy.
- **description** (string, optional): A human-readable description of the health check.
- **http_config** (object, optional): Parameters specific to an HTTP or HTTPS health check.
- **interval** (integer, optional): The interval between each health check. Shorter intervals may give quicker notifications if the origin status changes, but will increase load on the origin as we check from multiple locations.
- **name** (string, required): A short name to identify the health check. Only alphanumeric characters, hyphens and underscores are allowed.
- **retries** (integer, optional): The number of retries to attempt in case of a timeout before marking the origin as unhealthy. Retries are attempted immediately.
- **suspended** (boolean, optional): If suspended, no health checks are sent to the origin.
- **tcp_config** (object, optional): Parameters specific to TCP health check.
- **timeout** (integer, optional): The timeout (in seconds) before marking the health check as failed.
- **type** (string, optional): The protocol to use for the health check. Currently supported protocols are 'HTTP', 'HTTPS' and 'TCP'.

## Response

### 200

Create Health Check response.

- **result** (object, optional): 

### 4XX

Create Health Check response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
