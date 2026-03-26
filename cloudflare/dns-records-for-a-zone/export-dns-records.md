# Export DNS Records

`GET /zones/{zone_id}/dns_records/export`

You can export your [BIND config](https://en.wikipedia.org/wiki/Zone_file "Zone file") through this endpoint.

See [the documentation](https://developers.cloudflare.com/dns/manage-dns-records/how-to/import-and-export/ "Import and export records") for more information.

## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 200

Export DNS Records response

### 4XX

Export DNS Records response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
