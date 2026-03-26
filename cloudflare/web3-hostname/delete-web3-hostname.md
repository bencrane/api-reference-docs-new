# Delete Web3 Hostname

`DELETE /zones/{zone_id}/web3/hostnames/{identifier}`



## Parameters

- **identifier** (string, required) [path]: 
- **zone_id** (string, required) [path]: 


## Response

### 200

Delete Web3 Hostname response.

_Empty object_

### 4XX

Delete Web3 Hostname error response (4XX).

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Specifies whether the API call was successful. Values: `false`

### 5XX

Delete Web3 Hostname response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Specifies whether the API call was successful. Values: `false`
