# Get a Page Shield cookie

`GET /zones/{zone_id}/page_shield/cookies/{cookie_id}`

Fetches a cookie collected by Page Shield by cookie ID.

## Parameters

- **zone_id** (string, required) [path]: 
- **cookie_id** (string, required) [path]: 

## Response

### 200

Get a Page Shield cookie response

- **result** (object, optional): 

### 4XX

Get a Page Shield cookie response failure

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful
