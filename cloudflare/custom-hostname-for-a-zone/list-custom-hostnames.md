# List Custom Hostnames

`GET /zones/{zone_id}/custom_hostnames`

List, search, sort, and filter all of your custom hostnames.

## Parameters

- **zone_id** (string, required) [path]: 
- **hostname** (string, optional) [query]: 
- **hostname.contain** (string, optional) [query]: 
- **id** (string, optional) [query]: 
- **page** (number, optional) [query]: 
- **per_page** (number, optional) [query]: 
- **order** (string, optional) [query]: 
- **direction** (string, optional) [query]: 
- **ssl_status** (string, optional) [query]: 
- **hostname_status** (string, optional) [query]: 
- **certificate_authority** (string, optional) [query]: 
- **wildcard** (boolean, optional) [query]: 
- **custom_origin_server** (string, optional) [query]: 
- **ssl** (string, optional) [query]: 

## Response

### 200

List Custom Hostnames response

- **result** (array, optional): 

### 4XX

List Custom Hostnames response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
