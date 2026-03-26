# Fetch a meeting for an App

`GET /accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}`

Returns a meeting details in an App for the given meeting ID.

## Parameters

- **name** (string, optional) [query]: 
- **meeting_id** (string, required) [path]: ID of the meeting. Fetch the meeting ID using the create a meeting API.

## Response

### 200

Success Response

- **data** (object, optional): Data returned by the operation
- **success** (boolean, optional): Success status of the operation

### 500

Failure response

- **error** (object): 
- **success** (boolean): Success status of the request.
