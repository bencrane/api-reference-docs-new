# Get Logpush job details

`GET /zones/{zone_id}/logpush/jobs/{job_id}`

Gets the details of a Logpush job.

## Parameters

- **job_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Response

### 200

Get Logpush job details response.

- **result** (object, optional): 

### 4XX

Get Logpush job details response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
