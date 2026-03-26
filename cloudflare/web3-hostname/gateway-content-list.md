# Update IPFS Universal Path Gateway Content List

`PUT /zones/{zone_id}/web3/hostnames/{identifier}/ipfs_universal_path/content_list`



## Parameters

- **identifier** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Request Body

- **action** (string, required): Behavior of the content list. Values: `block`
- **entries** (array, required): Provides content list entries.

## Response

### 200

Update IPFS Universal Path Gateway Content List response.

- **result** (object, optional): 

### 4XX

Update IPFS Universal Path Gateway Content List error response (4XX).

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Specifies whether the API call was successful. Values: `false`

### 5XX

Update IPFS Universal Path Gateway Content List response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Specifies whether the API call was successful. Values: `false`
