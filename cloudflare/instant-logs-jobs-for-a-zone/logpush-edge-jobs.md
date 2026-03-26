# List Instant Logs jobs

`GET /zones/{zone_id}/logpush/edge/jobs`

Lists Instant Logs jobs for a zone.

## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 200

List Instant Logs jobs response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (array, optional): 

### 4XX

List Instant Logs jobs response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
