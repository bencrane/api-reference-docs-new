# Preview sending subdomain DNS

`POST /zones/{zone_id}/email/sending/subdomains/preview`

Returns the DNS records that would be created for a sending subdomain, flags which records are missing, and reports any conflicts with existing DNS records. This is a read-only dry-run — no records are created or modified. Use before or after creating a subdomain to check DNS status.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **name** (string, required): The subdomain name. Must be within the zone.

## Response

### 200

Preview sending subdomain DNS response

- **result** (object, optional):
