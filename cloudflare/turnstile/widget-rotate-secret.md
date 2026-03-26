# Rotate Secret for a Turnstile Widget

`POST /accounts/{account_id}/challenges/widgets/{sitekey}/rotate_secret`

Generate a new secret key for this widget. If `invalidate_immediately`
is set to `false`, the previous secret remains valid for 2 hours.

Note that secrets cannot be rotated again during the grace period.


## Request Body

- **invalidate_immediately** (boolean, optional): If `invalidate_immediately` is set to `false`, the previous secret will
remain valid for two hours. Otherwise, the secret is immediately
invalidated, and requests using it will be rejected.


## Response

### 200

Rotate Secret Response

_Empty object_

### 4XX

Rotate Secret Response Error

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful
