# Get information about a CNI object

`GET /accounts/{account_id}/cni/cnis/{cni}`



## Parameters

- **cni** (string, required) [path]: CNI ID to retrieve information about
- **account_id** (string, required) [path]: 

## Response

### 200

CNI's associated data

- **account** (string): Customer account tag
- **bgp** (object): 
- **cust_ip** (string): Customer end of the point-to-point link

This should always be inside the same prefix as `p2p_ip`.
- **id** (string): 
- **interconnect** (string): Interconnect identifier hosting this CNI
- **magic** (object): 
- **p2p_ip** (string): Cloudflare end of the point-to-point link

### 400

Bad request

### 404

CNI not found

### 500

Internal server error
