# Delete ACL

`DELETE /accounts/{account_id}/secondary_dns/acls/{acl_id}`

Delete ACL.

## Parameters

- **acl_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 


## Response

### 200

Delete ACL response.

_Empty object_

### 4XX

Delete ACL response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
