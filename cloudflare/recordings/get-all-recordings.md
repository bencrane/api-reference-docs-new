# Fetch all recordings for an App

`GET /accounts/{account_id}/realtime/kit/{app_id}/recordings`

Returns all recordings for an App. If the `meeting_id` parameter is passed, returns all recordings for the given meeting ID.

## Parameters

- **account_id** (string, required) [path]: 
- **app_id** (string, required) [path]: 
- **meeting_id** (string, optional) [query]: ID of a meeting. Optional. Will limit results to only this meeting if passed.
- **page_no** (number, optional) [query]: The page number from which you want your page search results to be displayed.
- **per_page** (number, optional) [query]: Number of results per page
- **expired** (boolean, optional) [query]: If passed, only shows expired/non-expired recordings on RealtimeKit's bucket
- **search** (string, optional) [query]: The search query string. You can search using the meeting ID or title.
- **sort_by** (string, optional) [query]: 
- **sort_order** (string, optional) [query]: 
- **start_time** (string, optional) [query]: The start time range for which you want to retrieve the meetings. The time must be specified in ISO format.
- **end_time** (string, optional) [query]: The end time range for which you want to retrieve the meetings. The time must be specified in ISO format.
- **status** (array, optional) [query]: Filter by one or more recording status

## Response

### 200

Success response

- **data** (array, optional): 
- **paging** (object, optional): 
- **success** (boolean, optional): 

### 201

Created
