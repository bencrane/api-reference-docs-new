# Delete Custom Hostname (and any issued SSL certificates)

`DELETE /zones/{zone_id}/custom_hostnames/{custom_hostname_id}`

Permanently deletes a custom hostname and revokes any SSL certificates that were issued for it. This action cannot be undone.

## Parameters

- **custom_hostname_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 


## Response

### 200

Delete Custom Hostname (and any issued SSL certificates) response

- **id** (string): Identifier.

### 4XX

Delete Custom Hostname (and any issued SSL certificates) response failure

- **id** (string, optional): Identifier.
- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
