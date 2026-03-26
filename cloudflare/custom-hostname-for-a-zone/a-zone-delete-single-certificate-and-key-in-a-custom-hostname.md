# Delete Single Certificate And Key For Custom Hostname

`DELETE /zones/{zone_id}/custom_hostnames/{custom_hostname_id}/certificate_pack/{certificate_pack_id}/certificates/{certificate_id}`

Delete a single custom certificate from a certificate pack that contains two bundled certificates. Deletion is subject to the following constraints. You cannot delete a certificate if it is the only remaining certificate in the pack. At least one certificate must remain in the pack.

## Parameters

- **custom_hostname_id** (string, required) [path]: 
- **certificate_pack_id** (string, required) [path]: 
- **certificate_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 


## Response

### 202

Delete Single Certificate and Key In a Custom Hostname response

- **id** (string): Identifier.

### 4XX

Delete Single Certificate and Key In a Custom Hostname response failure

- **id** (string, optional): Identifier.
- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
