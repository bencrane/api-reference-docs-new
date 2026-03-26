# IPFS Universal Path Gateway Content List Entry Details

`GET /zones/{zone_id}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries/{content_list_entry_identifier}`



## Parameters

- **content_list_entry_identifier** (string, required) [path]: 
- **identifier** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Response

### 200

IPFS Universal Path Gateway Content List Entry Details response.

- **result** (object, optional): Specify a content list entry to block.

### 4XX

IPFS Universal Path Gateway Content List Entry Details error response (4XX).

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Specifies whether the API call was successful. Values: `false`

### 5XX

IPFS Universal Path Gateway Content List Entry Details response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Specifies whether the API call was successful. Values: `false`
