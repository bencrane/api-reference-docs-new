# Fetch active livestreams for a meeting

`GET /accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/active-livestream`

Returns details of all active livestreams for the given meeting ID.

## Parameters

- **meeting_id** (string, required) [path]: ID of the meeting

## Response

### 200

OK

- **data** (object): 
- **success** (boolean):
