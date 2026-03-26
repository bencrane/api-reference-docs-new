# Delete Logpush job

`DELETE /accounts/{account_id}/logpush/jobs/{job_id}`

Deletes a Logpush job.

## Parameters

- **job_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 


## Response

### 200

Delete Logpush job response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Delete Logpush job response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
