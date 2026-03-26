# Start livestreaming a meeting

`POST /accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/livestreams`

Starts livestream of a meeting associated with the given meeting ID. Retreive the meeting ID using the `Create a meeting` API.

## Parameters

- **meeting_id** (string, required) [path]: ID of the meeting

## Request Body

- **name** (string, optional): 
- **video_config** (object, optional): 

## Response

### 201

Created

- **data** (object): 
- **success** (boolean):
