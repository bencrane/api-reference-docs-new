# Delete Site ACL

`DELETE /accounts/{account_id}/magic/sites/{site_id}/acls/{acl_id}`

Remove a specific Site ACL.

## Parameters

- **site_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 
- **acl_id** (string, required) [path]: 


## Response

### 200

Delete Site ACL response

- **result** (object, optional): Bidirectional ACL policy for network traffic within a site.

### 4XX

Delete Site ACL response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful
