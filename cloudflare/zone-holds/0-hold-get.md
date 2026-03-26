# Get Zone Hold

`GET /zones/{zone_id}/hold`

Retrieve whether the zone is subject to a zone hold, and metadata about the hold.

## Parameters

- **zone_id** (string, required) [path]: Zone ID

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
