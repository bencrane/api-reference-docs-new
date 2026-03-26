# Site ACL Details

`GET /accounts/{account_id}/magic/sites/{site_id}/acls/{acl_id}`

Get a specific Site ACL.

## Parameters

- **site_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 
- **acl_id** (string, required) [path]: 

## Response

### 200

Site ACL Details response

- **result** (object, optional): Bidirectional ACL policy for network traffic within a site.

### 4XX

Site ACL Details response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful
