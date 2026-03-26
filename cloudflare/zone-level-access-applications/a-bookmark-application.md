# Add an Access application

`POST /zones/{zone_id}/access/apps`

Adds a new application to Access.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

_Empty object_

## Response

### 201

Add an Access application response

- **result** (object, optional): 

### 4XX

Add an Access application response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
