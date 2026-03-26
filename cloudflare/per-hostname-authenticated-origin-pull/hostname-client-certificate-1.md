# Delete Hostname Client Certificate

`DELETE /zones/{zone_id}/origin_tls_client_auth/hostnames/certificates/{certificate_id}`

Removes a client certificate used for authenticated origin pulls on a specific hostname.
Note: Before deleting the certificate, you must first invalidate the hostname for client authentication by sending a PUT request with `enabled` set to null. After invalidating the association, the certificate can be safely deleted.


## Parameters

- **certificate_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 


## Response

### 200

Delete Hostname Client Certificate response

- **result** (object, optional): 

### 4XX

Delete Hostname Client Certificate response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
