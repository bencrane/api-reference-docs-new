# Enable Content Scanning

`POST /zones/{zone_id}/content-upload-scan/enable`

Enable Content Scanning.

## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 200

Enable Content Scanning response.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

### 4XX

Enable Content Scanning failure response.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
