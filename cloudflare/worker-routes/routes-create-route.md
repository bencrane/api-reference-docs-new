# Create Route

`POST /zones/{zone_id}/workers/routes`

Creates a route that maps a URL pattern to a Worker.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **id** (object, required): 
- **pattern** (string, required): Pattern to match incoming requests against. [Learn more](https://developers.cloudflare.com/workers/configuration/routing/routes/#matching-behavior).
- **script** (string, optional): Name of the script to run if the route matches.

## Response

### 200

Create Route response.

_Empty object_

### 4XX

Create Route response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
