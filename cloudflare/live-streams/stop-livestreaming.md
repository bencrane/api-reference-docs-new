# Stop livestreaming a meeting

`POST /accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/active-livestream/stop`

Stops the active livestream of a meeting associated with the given meeting ID. Retreive the meeting ID using the `Create a meeting` API.

## Parameters

- **meeting_id** (string, required) [path]: ID of the meeting


## Response

### 200

OK

- **data** (object): 
- **success** (boolean):
