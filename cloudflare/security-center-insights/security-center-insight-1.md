# Archives Zone Security Center Insight

`PUT /zones/{zone_id}/security-center/insights/{issue_id}/dismiss`

Archives a zone-specific Security Center insight, removing it from the active zone insights while preserving historical data.

## Parameters

- **zone_id** (string, required) [path]: 
- **issue_id** (string, required) [path]: 

## Request Body

- **dismiss** (boolean, optional): 

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
