# Table

`GET /zones/{zone_id}/dns_analytics/report`

Retrieves a list of summarised aggregate metrics over a given time period.

See [Analytics API properties](https://developers.cloudflare.com/dns/reference/analytics-api-properties/) for detailed information about the available query parameters.

## Parameters

- **zone_id** (string, required) [path]: 
- **metrics** (string, optional) [query]: 
- **dimensions** (string, optional) [query]: 
- **since** (string, optional) [query]: 
- **until** (string, optional) [query]: 
- **limit** (string, optional) [query]: 
- **sort** (string, optional) [query]: 
- **filters** (string, optional) [query]: 

## Response

### 200

Table response

_Empty object_

### 4XX

Table response failure

_Empty object_
