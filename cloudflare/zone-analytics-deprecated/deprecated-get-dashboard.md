# Get dashboard

`GET /zones/{zone_identifier}/analytics/dashboard`

> **Deprecated**

The dashboard view provides both totals and timeseries data for the given zone and time period across the entire Cloudflare network.

## Parameters

- **zone_identifier** (string, required) [path]: 
- **until** (string, optional) [query]: 
- **since** (string, optional) [query]: 
- **continuous** (boolean, optional) [query]: 

## Response

### 200

Get dashboard response

- **query** (object, optional): The exact parameters/timestamps the analytics service used to return data.
- **result** (object, optional): Totals and timeseries data.

### 4XX

Get dashboard response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
