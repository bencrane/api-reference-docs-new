# Update an Access application

`PUT /zones/{zone_id}/access/apps/{app_id}`

Updates an Access application.

## Parameters

- **app_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Request Body

_Empty object_

## Response

### 200

Update an Access application response

- **result** (object, optional): 

### 4XX

Update an Access application response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
