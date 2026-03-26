# Edit Web3 Hostname

`PATCH /zones/{zone_id}/web3/hostnames/{identifier}`



## Parameters

- **identifier** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Request Body

- **description** (string, optional): Specify an optional description of the hostname.
- **dnslink** (string, optional): Specify the DNSLink value used if the target is ipfs.

## Response

### 200

Edit Web3 Hostname response.

- **result** (object, optional): 

### 4XX

Edit Web3 Hostname error response (4XX).

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Specifies whether the API call was successful. Values: `false`

### 5XX

Edit Web3 Hostname response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Specifies whether the API call was successful. Values: `false`
