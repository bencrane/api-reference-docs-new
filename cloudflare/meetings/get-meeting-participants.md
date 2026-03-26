# Fetch all participants of a meeting

`GET /accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/participants`

Returns all participants detail for the given meeting ID.

## Parameters

- **account_id** (string, required) [path]: 
- **app_id** (string, required) [path]: 
- **page_no** (number, optional) [query]: The page number from which you want your page search results to be displayed.
- **per_page** (number, optional) [query]: Number of results per page
- **meeting_id** (string, required) [path]: ID of the meeting. Fetch the meeting ID using the create a meeting API.

## Response

### 200

Success response

- **data** (array, optional): 
- **paging** (object, optional): 
- **success** (boolean, optional): 

### 500

Failure response

- **error** (object): 
- **success** (boolean): Success status of the request.
