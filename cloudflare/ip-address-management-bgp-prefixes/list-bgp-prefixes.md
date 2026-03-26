# List BGP Prefixes

`GET /accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/prefixes`

List all BGP Prefixes within the specified IP Prefix. BGP Prefixes are used to control which specific subnets are advertised to the Internet. It is possible to advertise subnets more specific than an IP Prefix by creating more specific BGP Prefixes.

## Parameters

- **account_id** (string, required) [path]: 
- **prefix_id** (string, required) [path]: 

## Response

### 200

List BGP Prefixes response

- **result** (array, optional): 

### 4XX

List BGP Prefixes response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
