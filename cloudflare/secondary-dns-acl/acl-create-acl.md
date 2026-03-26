# Create ACL

`POST /accounts/{account_id}/secondary_dns/acls`

Create ACL.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **ip_range** (string, required): Allowed IPv4/IPv6 address range of primary or secondary nameservers. This will be applied for the entire account. The IP range is used to allow additional NOTIFY IPs for secondary zones and IPs Cloudflare allows AXFR/IXFR requests from for primary zones. CIDRs are limited to a maximum of /24 for IPv4 and /64 for IPv6 respectively.
- **name** (string, required): The name of the acl.

## Response

### 200

Create ACL response.

_Empty object_

### 4XX

Create ACL response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
