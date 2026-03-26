# Get analytics by Co-locations

`GET /zones/{zone_identifier}/analytics/colos`

> **Deprecated**

This view provides a breakdown of analytics data by datacenter. Note: This is available to Enterprise customers only.

## Parameters

- **zone_identifier** (string, required) [path]: 
- **until** (string, optional) [query]: 
- **since** (string, optional) [query]: 
- **continuous** (boolean, optional) [query]: 

## Response

### 200

Get analytics by Co-locations response

- **query** (object, optional): The exact parameters/timestamps the analytics service used to return data.
- **result** (array, optional): A breakdown of all dashboard analytics data by co-locations. This is limited to Enterprise zones only.

### 4XX

Get analytics by Co-locations response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
