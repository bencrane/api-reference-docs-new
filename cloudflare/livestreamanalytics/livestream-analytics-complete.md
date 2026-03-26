# Fetch complete analytics data for your livestreams

`GET /accounts/{account_id}/realtime/kit/{app_id}/analytics/livestreams/overall`

Returns livestream analytics for the specified time range.

## Parameters

- **account_id** (string, required) [path]: 
- **app_id** (string, required) [path]: 
- **start_time** (string, optional) [query]: Specify the start time range in ISO format to access the livestream analytics.
- **end_time** (string, optional) [query]: Specify the end time range in ISO format to access the livestream analytics.

## Response

### 200

OK

- **data** (object): 
- **success** (boolean):
