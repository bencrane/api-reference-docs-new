# Fetch details of a participant

`GET /accounts/{account_id}/realtime/kit/{app_id}/sessions/{session_id}/participants/{participant_id}`

Returns details of the given participant ID along with call statistics for the given session ID.

## Parameters

- **account_id** (string, required) [path]: 
- **app_id** (string, required) [path]: 
- **filters** (string, optional) [query]: Comma separated list of filters to apply. Note that there must be no spaces between the filters.
- **include_peer_events** (boolean, optional) [query]: if true, response includes all the peer events of participant.
- **participant_id** (string, required) [path]: ID of the participant
- **session_id** (string, required) [path]: ID of the session

## Response

### 200

Returns details of a participant along with callstats data.

- **data** (object): 
- **success** (boolean):
