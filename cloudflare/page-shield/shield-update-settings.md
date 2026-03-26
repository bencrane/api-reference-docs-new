# Update Page Shield settings

`PUT /zones/{zone_id}/page_shield`

Updates Page Shield settings.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **enabled** (boolean, optional): When true, indicates that Page Shield is enabled.
- **use_cloudflare_reporting_endpoint** (boolean, optional): When true, CSP reports will be sent to https://csp-reporting.cloudflare.com/cdn-cgi/script_monitor/report
- **use_connection_url_path** (boolean, optional): When true, the paths associated with connections URLs will also be analyzed.

## Response

### 200

Update Page Shield settings response

- **result** (object, optional): 

### 4XX

Update Page Shield settings response failure

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful
