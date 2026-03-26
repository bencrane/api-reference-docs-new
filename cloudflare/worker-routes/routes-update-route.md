# Update Route

`PUT /zones/{zone_id}/workers/routes/{route_id}`

Updates the URL pattern or Worker associated with a route.

## Parameters

- **route_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Request Body

- **id** (object, required): 
- **pattern** (string, required): Pattern to match incoming requests against. [Learn more](https://developers.cloudflare.com/workers/configuration/routing/routes/#matching-behavior).
- **script** (string, optional): Name of the script to run if the route matches.

## Response

### 200

Update Route response.

_Empty object_

### 4XX

Update Route response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
