# Delete a sending subdomain

`DELETE /zones/{zone_id}/email/sending/subdomains/{subdomain_id}`

Disables sending on a subdomain and removes its DNS records. If routing is still active on the subdomain, only sending is disabled.

## Parameters

- **subdomain_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Response

### 200

Delete a sending subdomain response

_Empty object_
