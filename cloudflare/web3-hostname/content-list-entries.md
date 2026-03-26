# List IPFS Universal Path Gateway Content List Entries

`GET /zones/{zone_id}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries`



## Parameters

- **identifier** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Response

### 200

List IPFS Universal Path Gateway Content List Entries response.

- **result** (object, optional): 

### 4XX

List IPFS Universal Path Gateway Content List Entries error response (4XX).

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Specifies whether the API call was successful. Values: `false`

### 5XX

List IPFS Universal Path Gateway Content List Entries response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Specifies whether the API call was successful. Values: `false`
