# Fetch livestream session details using a session ID

`GET /accounts/{account_id}/realtime/kit/{app_id}/sessions/{session_id}/livestream-sessions`

Returns livestream session details for the given session ID. Retreive the session ID using the `Fetch all sessions of an App` API.

## Parameters

- **account_id** (string, required) [path]: 
- **app_id** (string, required) [path]: 
- **per_page** (number, optional) [query]: Number of results per page.
- **page_no** (number, optional) [query]: The page number from which you want your page search results to be displayed.
- **session_id** (string, required) [path]: 

## Response

### 200

OK

- **data** (object): 
- **success** (boolean):
