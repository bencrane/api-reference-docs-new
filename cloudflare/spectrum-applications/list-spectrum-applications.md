# List Spectrum applications

`GET /zones/{zone_id}/spectrum/apps`

Retrieves a list of currently existing Spectrum applications inside a zone.

## Parameters

- **zone_id** (string, required) [path]: 
- **page** (number, optional) [query]: 
- **per_page** (number, optional) [query]: 
- **direction** (string, optional) [query]: 
- **order** (string, optional) [query]: 

## Response

### 200

List Spectrum applications response.

- **result** (object, optional): 

### 4XX

List Spectrum applications response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
