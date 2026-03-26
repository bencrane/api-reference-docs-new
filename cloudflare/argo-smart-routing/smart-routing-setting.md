# Get Argo Smart Routing setting

`GET /zones/{zone_id}/argo/smart_routing`

Retrieves the value of Argo Smart Routing enablement setting.

## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 200

Get Argo Smart Routing enablement setting response.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): Describes a successful API response.

### 4XX

Get Argo Smart Routing enablement setting failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Describes a failed API response. Values: `false`
