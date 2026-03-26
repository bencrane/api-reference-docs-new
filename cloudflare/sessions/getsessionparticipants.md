# Fetch participants list of a session

`GET /accounts/{account_id}/realtime/kit/{app_id}/sessions/{session_id}/participants`

Returns a list of participants for the given session ID.

## Parameters

- **account_id** (string, required) [path]: 
- **app_id** (string, required) [path]: 
- **search** (string, optional) [query]: The search query string. You can search using the meeting ID or title.
- **page_no** (number, optional) [query]: The page number from which you want your page search results to be displayed.
- **per_page** (number, optional) [query]: Number of results per page
- **sort_order** (string, optional) [query]: 
- **sort_by** (string, optional) [query]: 
- **include_peer_events** (boolean, optional) [query]: if true, response includes all the peer events of participants.
- **view** (string, optional) [query]: In breakout room sessions, the view parameter can be set to `raw` for session specific duration for participants or `consolidated` to accumulate breakout room durations.
- **session_id** (string, required) [path]: ID of the session

## Response

### 200

Get participants list of a particular session

- **data** (object): 
- **success** (boolean):
