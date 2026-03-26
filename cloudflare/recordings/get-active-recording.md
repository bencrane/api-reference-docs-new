# Fetch active recording

`GET /accounts/{account_id}/realtime/kit/{app_id}/recordings/active-recording/{meeting_id}`

Returns the active recording details for the given meeting ID.

## Parameters

- **account_id** (string, required) [path]: 
- **app_id** (string, required) [path]: 
- **meeting_id** (string, required) [path]: ID of the meeting

## Response

### 200

Success response

- **data** (object, optional): 
- **success** (boolean, optional): Success status of the operation

### 404

Failure response

- **error** (object): 
- **success** (boolean): Success status of the request.
