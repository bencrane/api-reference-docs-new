# Retrieves Zone Security Center Insight Counts by Severity

`GET /zones/{zone_id}/security-center/insights/severity`

Retrieves zone-specific Security Center insight counts aggregated by severity level.

## Parameters

- **zone_id** (string, required) [path]: 
- **dismissed** (string, optional) [query]: 
- **issue_class** (string, optional) [query]: 
- **issue_type** (string, optional) [query]: 
- **product** (string, optional) [query]: 
- **severity** (string, optional) [query]: 
- **subject** (string, optional) [query]: 
- **issue_class~neq** (string, optional) [query]: 
- **issue_type~neq** (string, optional) [query]: 
- **product~neq** (string, optional) [query]: 
- **severity~neq** (string, optional) [query]: 
- **subject~neq** (string, optional) [query]: 

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
