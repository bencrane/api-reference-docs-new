# Update Health Check

`PUT /zones/{zone_id}/smart_shield/healthchecks/{healthcheck_id}`

Update a configured health check.

## Parameters

- **healthcheck_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Request Body

- **result** (object, optional): 

## Response

### 200

Update Health Check response.

- **result** (object, optional): 

### 4XX

Update Health Check response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
