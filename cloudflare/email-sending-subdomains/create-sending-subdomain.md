# Create a sending subdomain

`POST /zones/{zone_id}/email/sending/subdomains`

Creates a new sending subdomain or re-enables sending on an existing subdomain that had it disabled. If zone-level Email Sending has not been enabled yet, the zone flag is automatically set when the entitlement is present.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **name** (string, required): The subdomain name. Must be within the zone.

## Response

### 200

Create a sending subdomain response

- **result** (object, optional):
