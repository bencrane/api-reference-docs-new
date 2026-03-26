# Health Check Details

`GET /zones/{zone_id}/smart_shield/healthchecks/{healthcheck_id}`

Fetch a single configured health check.

## Parameters

- **healthcheck_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Response

### 200

Health Check Details response.

- **result** (object, optional): 

### 4XX

Health Check Details response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
