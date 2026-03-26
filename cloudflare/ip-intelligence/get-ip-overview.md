# Get IP Overview

`GET /accounts/{account_id}/intel/ip`

Gets the geolocation, ASN, infrastructure type of the ASN, and any security threat categories of an IP address. **Must provide ip query parameters.** For example, `/intel/ip?ipv4=1.1.1.1` or `/intel/ip?ipv6=2001:db8::1`.

## Parameters

- **account_id** (string, required) [path]: 
- **ipv4** (string, optional) [query]: 
- **ipv6** (string, optional) [query]: 

## Response

### 200

Get IP Overview response.

_Empty object_

### 4XX

Get IP Overview response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful.
