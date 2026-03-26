# Fetch livestream session details for a meeting

`GET /accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/livestream`

Returns livestream session details for the given meeting ID. Retreive the meeting ID using the `Create a meeting` API.

## Parameters

- **page_no** (integer, optional) [query]: The page number from which you want your page search results to be displayed.
- **per_page** (integer, optional) [query]: Number of results per page.
- **meeting_id** (string, required) [path]: ID of the meeting

## Response

### 200

OK

- **data** (object): 
- **success** (boolean):
