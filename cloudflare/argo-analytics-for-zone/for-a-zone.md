# Argo Analytics for a zone

`GET /zones/{zone_id}/analytics/latency`



## Parameters

- **zone_id** (string, required) [path]: 
- **bins** (string, optional) [query]: 

## Response

### 200

Argo Analytics for a zone response

- **result** (object, optional): 

### 4XX

Argo Analytics for a zone response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
