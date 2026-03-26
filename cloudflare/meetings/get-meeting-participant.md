# Fetch a participant's detail

`GET /accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/participants/{participant_id}`

Returns a participant details for the given meeting and participant ID.

## Parameters

- **meeting_id** (string, required) [path]: ID of the meeting. You can fetch the meeting ID using the create a meeting API.
- **participant_id** (string, required) [path]: ID of the participant. You can fetch the participant ID using the add a participant API.

## Response

### 200

Success response

- **data** (object, optional): Represents a participant.
- **success** (boolean, optional): Success status of the operation

### 500

Failure response

- **error** (object): 
- **success** (boolean): Success status of the request.
