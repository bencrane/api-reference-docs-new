# Fetch livestream details using livestream ID

`GET /accounts/{account_id}/realtime/kit/{app_id}/livestreams/{livestream_id}`

Returns details of a livestream with sessions for the given livestream ID. Retreive the livestream ID using the `Start livestreaming a meeting` API.

## Parameters

- **account_id** (string, required) [path]: 
- **app_id** (string, required) [path]: 
- **page_no** (integer, optional) [query]: The page number from which you want your page search results to be displayed.
- **per_page** (integer, optional) [query]: Number of results per page.
- **livestream_id** (string, required) [path]: 

## Response

### 200

OK

- **data** (object): 
- **success** (boolean):
