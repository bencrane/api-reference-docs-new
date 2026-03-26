# Fetch day-wise session and recording analytics data for an App

`GET /accounts/{account_id}/realtime/kit/{app_id}/analytics/daywise`

Returns day-wise session and recording analytics data of an App for the specified time range start_date to end_date. If start_date and end_date are not provided, the default time range is set from 30 days ago to the current date.

## Parameters

- **account_id** (string, required) [path]: 
- **app_id** (string, required) [path]: 
- **start_date** (string, optional) [query]: start date in YYYY-MM-DD format
- **end_date** (string, optional) [query]: end date in YYYY-MM-DD format

## Response

### 200

OK

- **data** (object): 
- **success** (boolean):
