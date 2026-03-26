# Updates security.txt

`PUT /zones/{zone_id}/security-center/securitytxt`

Updates the security.txt file configuration for a zone, which provides security researchers with vulnerability reporting information.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **acknowledgments** (array, optional): 
- **canonical** (array, optional): 
- **contact** (array, optional): 
- **enabled** (boolean, optional): 
- **encryption** (array, optional): 
- **expires** (string, optional): 
- **hiring** (array, optional): 
- **policy** (array, optional): 
- **preferred_languages** (string, optional): 

## Response

### 200

The request was successful.

_Empty object_

### 4XX

A client error occurred.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
