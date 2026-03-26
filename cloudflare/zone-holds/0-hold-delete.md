# Remove Zone Hold

`DELETE /zones/{zone_id}/hold`

Stop enforcement of a zone hold on the zone, permanently or temporarily, allowing the
creation and activation of zones with this zone's hostname.

## Parameters

- **zone_id** (string, required) [path]: Zone ID
- **hold_after** (string, optional) [query]: If `hold_after` is provided, the hold will be temporarily disabled,
then automatically re-enabled by the system at the time specified
in this RFC3339-formatted timestamp. Otherwise, the hold will be
disabled indefinitely.

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
