# Create a new CNI object

`POST /accounts/{account_id}/cni/cnis`



## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **account** (string, required): Customer account tag
- **bgp** (object, optional): 
- **interconnect** (string, required): 
- **magic** (object, required): 

## Response

### 200

CNI was successfully created

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

### 409

Name Conflict

### 500

Internal server error
