# Retrieves security.txt

`GET /zones/{zone_id}/security-center/securitytxt`

Retrieves the current security.txt file configuration for a zone, used for security vulnerability reporting.

## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 200

The request was successful.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

A client error occurred.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
