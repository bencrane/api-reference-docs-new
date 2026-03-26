# Create a poll

`POST /accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/active-session/poll`

Creates a new poll in an active session for the given meeting ID.

## Parameters

- **account_id** (string, required) [path]: 
- **app_id** (string, required) [path]: 
- **meeting_id** (string, required) [path]: ID of the meeting

## Request Body

- **anonymous** (boolean, optional): if voters on a poll are anonymous
- **hide_votes** (boolean, optional): if votes on an option are visible before a person votes
- **options** (array, required): Different options for the question
- **question** (string, required): Question of the poll

## Response

### 201

response for creating a poll

- **data** (object): 
- **success** (boolean): 

### 400

Bad Request
