# Update Site ACL

`PUT /accounts/{account_id}/magic/sites/{site_id}/acls/{acl_id}`

Update a specific Site ACL.

## Parameters

- **site_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 
- **acl_id** (string, required) [path]: 

## Request Body

- **description** (string, optional): Description for the ACL.
- **forward_locally** (boolean, optional): The desired forwarding action for this ACL policy. If set to "false", the policy will forward traffic to Cloudflare. If set to "true", the policy will forward traffic locally on the Magic Connector. If not included in request, will default to false.
- **lan_1** (object, optional): 
- **lan_2** (object, optional): 
- **name** (string, optional): The name of the ACL.
- **protocols** (array, optional): 
- **unidirectional** (boolean, optional): The desired traffic direction for this ACL policy. If set to "false", the policy will allow bidirectional traffic. If set to "true", the policy will only allow traffic in one direction. If not included in request, will default to false.

## Response

### 200

Update Site ACL response

- **result** (object, optional): Bidirectional ACL policy for network traffic within a site.

### 4XX

Update Site ACL response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful
