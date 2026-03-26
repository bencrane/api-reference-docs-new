# ACL Details

`GET /accounts/{account_id}/secondary_dns/acls/{acl_id}`

Get ACL.

## Parameters

- **acl_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

ACL Details response.

_Empty object_

### 4XX

ACL Details response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
