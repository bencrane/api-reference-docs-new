# Create IPFS Universal Path Gateway Content List Entry

`POST /zones/{zone_id}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries`



## Parameters

- **identifier** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Request Body

- **content** (string, required): Specify the CID or content path of content to block.
- **description** (string, optional): Specify an optional description of the content list entry.
- **type** (string, required): Specify the type of content list entry to block. Values: `cid`, `content_path`

## Response

### 200

Create IPFS Universal Path Gateway Content List Entry response.

- **result** (object, optional): Specify a content list entry to block.

### 4XX

Create IPFS Universal Path Gateway Content List Entry error response (4XX).

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Specifies whether the API call was successful. Values: `false`

### 5XX

Create IPFS Universal Path Gateway Content List Entry response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Specifies whether the API call was successful. Values: `false`
