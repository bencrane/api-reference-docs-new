# List waiting rooms for account

`GET /accounts/{account_id}/waiting_rooms`

Lists waiting rooms for account.

## Parameters

- **account_id** (string, required) [path]: 
- **page** (number, optional) [query]: Page number of paginated results.
- **per_page** (number, optional) [query]: Maximum number of results per page. Must be a multiple of 5.

## Response

### 200

List waiting rooms for account response

_Empty object_

### 4XX

List waiting rooms for account response failure

_Empty object_
