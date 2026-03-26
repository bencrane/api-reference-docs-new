# Health Check Preview Details

`GET /zones/{zone_id}/healthchecks/preview/{healthcheck_id}`

Fetch a single configured health check preview.

## Parameters

- **healthcheck_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Response

### 200

Health Check Preview Details response.

- **result** (object, optional): 

### 4XX

Health Check Preview Details response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
