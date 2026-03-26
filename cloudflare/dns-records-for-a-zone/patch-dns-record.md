# Update DNS Record

`PATCH /zones/{zone_id}/dns_records/{dns_record_id}`

Update an existing DNS record.

Notes:
- A/AAAA records cannot exist on the same name as CNAME records.
- NS records cannot exist on the same name as any other record type.
- Domain names are always represented in Punycode, even if Unicode
  characters were used when creating the record.


## Parameters

- **dns_record_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Request Body

_Empty object_

## Response

### 200

Patch DNS Record response

_Empty object_

### 4XX

Patch DNS Record response failure

_Empty object_
