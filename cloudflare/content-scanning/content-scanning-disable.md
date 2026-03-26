# Disable Content Scanning

`POST /zones/{zone_id}/content-upload-scan/disable`

Disable Content Scanning.

## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 200

Disable Content Scanning response.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

### 4XX

Disable Content Scanning failure response.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
