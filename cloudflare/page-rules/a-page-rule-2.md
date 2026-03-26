# Get a Page Rule

`GET /zones/{zone_id}/pagerules/{pagerule_id}`

Fetches the details of a Page Rule.

## Parameters

- **pagerule_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Response

### 200

Get a Page Rule response

- **result** (object, optional): 

### 4XX

Get a Page Rule response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
