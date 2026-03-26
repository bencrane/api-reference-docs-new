# By Time

`GET /zones/{zone_id}/dns_analytics/report/bytime`

Retrieves a list of aggregate metrics grouped by time interval.

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
- **time_delta** (string, optional) [query]: 

## Response

### 200

By Time response

_Empty object_

### 4XX

By Time response failure

_Empty object_
