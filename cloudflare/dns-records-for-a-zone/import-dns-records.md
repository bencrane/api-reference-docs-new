# Import DNS Records

`POST /zones/{zone_id}/dns_records/import`

You can upload your [BIND config](https://en.wikipedia.org/wiki/Zone_file "Zone file") through this endpoint. It assumes that cURL is called from a location with bind_config.txt (valid BIND config) present.

See [the documentation](https://developers.cloudflare.com/dns/manage-dns-records/how-to/import-and-export/ "Import and export records") for more information.

## Parameters

- **zone_id** (string, required) [path]: 


## Response

### 200

Import DNS Records response

_Empty object_

### 4XX

Import DNS Records response failure

_Empty object_
