# Create Web3 Hostname

`POST /zones/{zone_id}/web3/hostnames`



## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **description** (string, optional): Specify an optional description of the hostname.
- **dnslink** (string, optional): Specify the DNSLink value used if the target is ipfs.
- **name** (string, required): Specify the hostname that points to the target gateway via CNAME.
- **target** (string, required): Specify the target gateway of the hostname. Values: `ethereum`, `ipfs`, `ipfs_universal_path`

## Response

### 200

Create Web3 Hostname response.

- **result** (object, optional): 

### 4XX

Create Web3 Hostname error response (4XX).

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Specifies whether the API call was successful. Values: `false`

### 5XX

Create Web3 Hostname response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Specifies whether the API call was successful. Values: `false`
