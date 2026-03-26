# Create Spectrum application using a name for the origin

`POST /zones/{zone_id}/spectrum/apps`

Creates a new Spectrum application from a configuration using a name for the origin.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

One of: Variant 1, Variant 2

## Response

### 200

Create Spectrum application using a name for the origin response.

- **result** (object, optional): 

### 4XX

Create Spectrum application using a name for the origin response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
