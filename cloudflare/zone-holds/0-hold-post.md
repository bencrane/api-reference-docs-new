# Create Zone Hold

`POST /zones/{zone_id}/hold`

Enforce a zone hold on the zone, blocking the creation and activation of zones with this zone's hostname.

## Parameters

- **zone_id** (string, required) [path]: Zone ID
- **include_subdomains** (boolean, optional) [query]: If provided, the zone hold will extend to block any subdomain of the given zone, as well
as SSL4SaaS Custom Hostnames. For example, a zone hold on a zone with the hostname
'example.com' and include_subdomains=true will block 'example.com',
'staging.example.com', 'api.staging.example.com', etc.

## Response

### 200

Successful Response

- **result** (object, optional): 

### 4XX

Client Error

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
