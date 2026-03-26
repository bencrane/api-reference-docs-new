# Fetch all meetings for an App

`GET /accounts/{account_id}/realtime/kit/{app_id}/meetings`

Returns all meetings for the given App ID.

## Parameters

- **account_id** (string, required) [path]: 
- **app_id** (string, required) [path]: 
- **page_no** (number, optional) [query]: The page number from which you want your page search results to be displayed.
- **per_page** (number, optional) [query]: Number of results per page
- **start_time** (string, optional) [query]: The start time range for which you want to retrieve the meetings. The time must be specified in ISO format.
- **end_time** (string, optional) [query]: The end time range for which you want to retrieve the meetings. The time must be specified in ISO format.
- **search** (string, optional) [query]: The search query string. You can search using the meeting ID or title.

## Response

### 200

Success response

- **data** (array, optional): 
- **paging** (object, optional): 
- **success** (boolean, optional):
