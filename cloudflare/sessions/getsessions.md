# Fetch all sessions of an App

`GET /accounts/{account_id}/realtime/kit/{app_id}/sessions`

Returns details of all sessions of an App.

## Parameters

- **account_id** (string, required) [path]: 
- **app_id** (string, required) [path]: 
- **page_no** (number, optional) [query]: The page number from which you want your page search results to be displayed.
- **per_page** (number, optional) [query]: Number of results per page
- **sort_by** (string, optional) [query]: 
- **sort_order** (string, optional) [query]: 
- **start_time** (string, optional) [query]: The start time range for which you want to retrieve the meetings. The time must be specified in ISO format.
- **end_time** (string, optional) [query]: The end time range for which you want to retrieve the meetings. The time must be specified in ISO format.
- **participants** (string, optional) [query]: 
- **status** (string, optional) [query]: 
- **search** (string, optional) [query]: Search string that matches sessions based on meeting title, meeting ID, and session ID
- **associated_id** (string, optional) [query]: ID of the meeting that sessions should be associated with

## Response

### 200

Get all sessions success response

- **data** (object): 
- **success** (boolean):
