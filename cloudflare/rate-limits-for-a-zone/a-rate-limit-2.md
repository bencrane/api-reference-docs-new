# Get a rate limit

`GET /zones/{zone_id}/rate_limits/{rate_limit_id}`

> **Deprecated**

Fetches the details of a rate limit.

## Parameters

- **rate_limit_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Response

### 200

Get a rate limit response.

- **result** (object, optional): 

### 4XX

Get a rate limit response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
