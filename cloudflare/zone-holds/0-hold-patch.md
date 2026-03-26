# Update Zone Hold

`PATCH /zones/{zone_id}/hold`

Update the `hold_after` and/or `include_subdomains` values on an existing zone hold.
The hold is enabled if the `hold_after` date-time value is in the past.

## Parameters

- **zone_id** (string, required) [path]: Zone ID

## Request Body

- **hold_after** (string, optional): If `hold_after` is provided and future-dated, the hold will be temporarily disabled,
then automatically re-enabled by the system at the time specified
in this RFC3339-formatted timestamp. A past-dated `hold_after` value will have
no effect on an existing, enabled hold. Providing an empty string will set its value
to the current time.
- **include_subdomains** (boolean, optional): If `true`, the zone hold will extend to block any subdomain of the given zone, as well
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
