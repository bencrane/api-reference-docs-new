# List rate limits

`GET /zones/{zone_id}/rate_limits`

> **Deprecated**

Fetches the rate limits for a zone.

## Parameters

- **zone_id** (string, required) [path]: 
- **page** (number, optional) [query]: 
- **per_page** (number, optional) [query]: 

## Response

### 200

List rate limits response.

- **result** (array, optional): 

### 4XX

List rate limits response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
