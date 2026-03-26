# Edit multiple zone settings

`PATCH /zones/{zone_id}/settings`

> **Deprecated**

Edit settings for a zone.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

Array of object

## Response

### 200

Edit zone settings info response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful
- **result** (array, optional): 

### 4XX

Edit zone settings info response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful
