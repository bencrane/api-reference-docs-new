# Refresh participant's authentication token

`POST /accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/participants/{participant_id}/token`

Regenerates participant's authentication token for the given meeting and participant ID.

## Parameters

- **account_id** (string, required) [path]: 
- **app_id** (string, required) [path]: 
- **meeting_id** (string, required) [path]: ID of the meeting. You can fetch the meeting ID using the create a meeting API.
- **participant_id** (string, required) [path]: ID of the participant. You can fetch the participant ID using the add a  participant API.

## Response

### 200

Example response

- **data** (object, optional): 
- **success** (boolean, optional): Success status of the operation

### 500

Failure response

- **error** (object): 
- **success** (boolean): Success status of the request.
