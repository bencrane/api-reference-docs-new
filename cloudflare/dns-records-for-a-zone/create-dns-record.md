# Create DNS Record

`POST /zones/{zone_id}/dns_records`

Create a new DNS record for a zone.

Notes:
- A/AAAA records cannot exist on the same name as CNAME records.
- NS records cannot exist on the same name as any other record type.
- Domain names are always represented in Punycode, even if Unicode
  characters were used when creating the record.


## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

_Empty object_

## Response

### 200

Create DNS Record response

_Empty object_

### 4XX

Create DNS Record response failure

_Empty object_
