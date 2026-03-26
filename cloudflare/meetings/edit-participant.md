# Edit a participant's detail

`PATCH /accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/participants/{participant_id}`

Updates a participant's details for the given meeting and participant ID.

## Parameters

- **meeting_id** (string, required) [path]: ID of the meeting. You can fetch the meeting ID using the create a meeting API.
- **participant_id** (string, required) [path]: ID of the participant. You can fetch the participant ID using the add a participant API.

## Request Body

- **name** (string, optional): (Optional) Name of the participant.
- **picture** (string, optional): (Optional) A URL to a picture to be used for the participant.
- **preset_name** (string, optional): (Optional) Name of the preset to apply to this participant.

## Response

### 200

Success response

- **data** (object, optional): 
- **success** (boolean, optional): Success status of the operation

### 500

Failure response

- **error** (object): 
- **success** (boolean): Success status of the request.
