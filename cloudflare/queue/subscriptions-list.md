# List Event Subscriptions

`GET /accounts/{account_id}/event_subscriptions/subscriptions`

Get a paginated list of event subscriptions with optional sorting and filtering

## Parameters

- **account_id** (string, required) [path]: 
- **page** (integer, optional) [query]: Page number for pagination
- **per_page** (integer, optional) [query]: Number of items per page
- **order** (string, optional) [query]: Field to sort by
- **direction** (string, optional) [query]: Sort direction

## Response

### 200

List of event subscriptions

_Empty object_

### 4XX

Failure response

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Indicates if the API call was successful or not.
