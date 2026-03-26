# Delete Health Check

`DELETE /zones/{zone_id}/healthchecks/{healthcheck_id}`

Delete a health check.

## Parameters

- **healthcheck_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 


## Response

### 200

Delete Health Check response.

- **result** (object, optional): 

### 4XX

Delete Health Check response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
