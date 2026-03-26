# Fetch all livestreams

`GET /accounts/{account_id}/realtime/kit/{app_id}/livestreams`

Returns details of livestreams associated with the given App ID. It includes livestreams created by your App and RealtimeKit meetings that are livestreamed by your App. If you only want details of livestreams created by your App and not RealtimeKit meetings, you can use the `exclude_meetings` query parameter.

## Parameters

- **exclude_meetings** (boolean, optional) [query]: Exclude the RealtimeKit meetings that are livestreamed.
- **per_page** (integer, optional) [query]: Number of results per page.
- **page_no** (integer, optional) [query]: The page number from which you want your page search results to be displayed.
- **status** (string, optional) [query]: Specifies the status of the operation.
- **start_time** (string, optional) [query]: Specify the start time range in ISO format to access the live stream.
- **end_time** (string, optional) [query]: Specify the end time range in ISO format to access the live stream.
- **sort_order** (string, optional) [query]: Specifies the sorting order for the results.

## Response

### 200

OK

- **data** (object): 
- **success** (boolean):
