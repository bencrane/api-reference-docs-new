# Patch Argo Smart Routing setting

`PATCH /zones/{zone_id}/argo/smart_routing`

Configures the value of the Argo Smart Routing enablement setting.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **value** (string, required): Specifies the enablement value of Argo Smart Routing. Values: `on`, `off`

## Response

### 200

Patch Argo Smart Routing enablement setting response.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): Describes a successful API response.

### 4XX

Patch Argo Smart Routing enablement setting failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Describes a failed API response. Values: `false`
