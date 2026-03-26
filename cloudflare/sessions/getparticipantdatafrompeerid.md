# Fetch details of peer

`GET /accounts/{account_id}/realtime/kit/{app_id}/sessions/peer-report/{peer_id}`

Returns details of the given peer ID along with call statistics for the given session ID.

## Parameters

- **account_id** (string, required) [path]: 
- **app_id** (string, required) [path]: 
- **filters** (string, optional) [query]: Comma separated list of filters to apply. Note that there must be no spaces between the filters.
- **peer_id** (string, required) [path]: ID of the peer

## Response

### 200

Returns details of a participant (using peer id) along with callstats data.

- **data** (object): 
- **success** (boolean):
