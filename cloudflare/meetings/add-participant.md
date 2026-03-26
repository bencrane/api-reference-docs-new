# Add a participant

`POST /accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/participants`

Adds a participant to the given meeting ID.

## Parameters

- **account_id** (string, required) [path]: 
- **app_id** (string, required) [path]: 
- **meeting_id** (string, required) [path]: ID of the meeting. Fetch the meeting ID using the create a meeting API.

## Request Body

- **custom_participant_id** (string, required): A unique participant ID. You must specify a unique ID for the participant, for example, UUID, email address, and so on. 
- **name** (string, optional): (Optional) Name of the participant. 
- **picture** (string, optional): (Optional) A URL to a picture to be used for the participant. 
- **preset_name** (string, required): Name of the preset to apply to this participant.

## Response

### 201

Success response

- **data** (object, optional): 
- **success** (boolean, optional): Success status of the operation

### 500

Failure response

- **error** (object): 
- **success** (boolean): Success status of the request.
