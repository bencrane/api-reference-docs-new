# Web3 Hostname Details

`GET /zones/{zone_id}/web3/hostnames/{identifier}`



## Parameters

- **identifier** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Response

### 200

Web3 Hostname Details response.

- **result** (object, optional): 

### 4XX

Web3 Hostname Details error response (4XX).

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Specifies whether the API call was successful. Values: `false`

### 5XX

Web3 Hostname Details response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Specifies whether the API call was successful. Values: `false`
