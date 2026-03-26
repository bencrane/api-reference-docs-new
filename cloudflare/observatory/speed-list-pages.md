# List tested webpages

`GET /zones/{zone_id}/speed_api/pages`

Lists all webpages which have been tested.

## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 200

List of pages.

- **result** (array, optional): 

### 4XX

Failure response.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
