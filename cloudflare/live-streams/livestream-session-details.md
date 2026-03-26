# Fetch active livestream session details

`GET /accounts/{account_id}/realtime/kit/{app_id}/livestreams/{livestream_id}/active-livestream-session`

Returns details of all active livestreams for the given livestream ID. Retreive the livestream ID using the `Start livestreaming a meeting` API.

## Parameters

- **account_id** (string, required) [path]: 
- **app_id** (string, required) [path]: 
- **livestream_id** (string, required) [path]: 

## Response

### 200

OK

- **data** (object): 
- **success** (boolean):
