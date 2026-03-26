# Preview Pool

`POST /accounts/{account_id}/load_balancers/pools/{pool_id}/preview`

Preview pool health using provided monitor details. The returned preview_id can be used in the preview endpoint to retrieve the results.

## Parameters

- **pool_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

- **allow_insecure** (boolean, optional): Do not validate the certificate when monitor use HTTPS. This parameter is currently only valid for HTTP and HTTPS monitors.
- **consecutive_down** (integer, optional): To be marked unhealthy the monitored origin must fail this healthcheck N consecutive times.
- **consecutive_up** (integer, optional): To be marked healthy the monitored origin must pass this healthcheck N consecutive times.
- **description** (string, optional): Object description.
- **expected_body** (string, optional): A case-insensitive sub-string to look for in the response body. If this string is not found, the origin will be marked as unhealthy. This parameter is only valid for HTTP and HTTPS monitors.
- **expected_codes** (string, optional): The expected HTTP response code or code range of the health check. This parameter is only valid for HTTP and HTTPS monitors.
- **follow_redirects** (boolean, optional): Follow redirects if returned by the origin. This parameter is only valid for HTTP and HTTPS monitors.
- **header** (object, optional): The HTTP request headers to send in the health check. It is recommended you set a Host header by default. The User-Agent header cannot be overridden. This parameter is only valid for HTTP and HTTPS monitors.
- **interval** (integer, optional): The interval between each health check. Shorter intervals may improve failover time, but will increase load on the origins as we check from multiple locations.
- **method** (string, optional): The method to use for the health check. This defaults to 'GET' for HTTP/HTTPS based checks and 'connection_established' for TCP based health checks.
- **path** (string, optional): The endpoint path you want to conduct a health check against. This parameter is only valid for HTTP and HTTPS monitors.
- **port** (integer, optional): The port number to connect to for the health check. Required for TCP, UDP, and SMTP checks. HTTP and HTTPS checks should only define the port when using a non-standard port (HTTP: default 80, HTTPS: default 443).
- **probe_zone** (string, optional): Assign this monitor to emulate the specified zone while probing. This parameter is only valid for HTTP and HTTPS monitors.
- **retries** (integer, optional): The number of retries to attempt in case of a timeout before marking the origin as unhealthy. Retries are attempted immediately.
- **timeout** (integer, optional): The timeout (in seconds) before marking the health check as failed.
- **type** (string, optional): The protocol to use for the health check. Currently supported protocols are 'HTTP','HTTPS', 'TCP', 'ICMP-PING', 'UDP-ICMP', and 'SMTP'. Values: `http`, `https`, `tcp`, `udp_icmp`, `icmp_ping`, `smtp`

## Response

### 200

Preview Pool response.

- **result** (object, optional): 

### 4XX

Preview Pool response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
