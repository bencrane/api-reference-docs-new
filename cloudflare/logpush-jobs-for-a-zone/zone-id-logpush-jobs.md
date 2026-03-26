# List Logpush jobs

`GET /zones/{zone_id}/logpush/jobs`

Lists Logpush jobs for a zone.

## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 200

List Logpush jobs response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (array, optional): 

### 4XX

List Logpush jobs response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
