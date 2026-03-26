# Rules

`GET /zones/{zone_id}/cloud_connector/rules`



## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 200

Cloud Connector rules response

_Empty object_

### 4XX

Cloud Connector response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

### 5XX

Cloud Connector response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
