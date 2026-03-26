# Get Access authentication logs

`GET /accounts/{account_id}/access/logs/access_requests`

Gets a list of Access authentication audit logs for an account.

## Parameters

- **account_id** (string, required) [path]: 
- **limit** (integer, optional) [query]: The maximum number of log entries to retrieve.
- **direction** (string, optional) [query]: The chronological sorting order for the logs.
- **since** (string, optional) [query]: The earliest event timestamp to query.
- **until** (string, optional) [query]: The latest event timestamp to query.
- **page** (integer, optional) [query]: 
- **per_page** (integer, optional) [query]: 
- **email** (string, optional) [query]: Filter by user email. Defaults to substring matching. To force exact matching, set `email_exact=true`.
Example (default): `email=@example.com` returns all events with that domain.
Example (exact): `email=user@example.com&email_exact=true` returns only that user.

- **email_exact** (boolean, optional) [query]: When true, `email` is matched exactly instead of substring matching.
- **user_id** (string, optional) [query]: Filter by user UUID.

- **allowedOp** (string, optional) [query]: Operator for the `allowed` filter.
- **country_codeOp** (string, optional) [query]: Operator for the `country_code` filter.
- **app_typeOp** (string, optional) [query]: Operator for the `app_type` filter.
- **app_uidOp** (string, optional) [query]: Operator for the `app_uid` filter.
- **ray_idOp** (string, optional) [query]: Operator for the `ray_id` filter.
- **emailOp** (string, optional) [query]: Operator for the `email` filter.
- **idpOp** (string, optional) [query]: Operator for the `idp` filter.
- **non_identityOp** (string, optional) [query]: Operator for the `non_identity` filter.
- **user_idOp** (string, optional) [query]: Operator for the `user_id` filter.
- **fields** (string, optional) [query]: Comma-separated list of fields to include in the response.
When omitted, all fields are returned.


## Response

### 200

Get Access authentication logs response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (array, optional): 

### 4XX

Get Access authentication logs response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
