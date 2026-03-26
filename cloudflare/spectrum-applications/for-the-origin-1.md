# Update Spectrum application configuration using a name for the origin

`PUT /zones/{zone_id}/spectrum/apps/{app_id}`

Updates a previously existing application's configuration that uses a name for the origin.

## Parameters

- **app_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Request Body

One of: Variant 1, Variant 2

## Response

### 200

Update Spectrum application configuration using a name for the origin response.

- **result** (object, optional): 

### 4XX

Update Spectrum application configuration using a name for the origin response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
