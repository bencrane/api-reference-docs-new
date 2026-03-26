# Read a saved event query

`GET /accounts/{account_id}/cloudforce-one/events/queries/{query_id}`

Retrieve a saved event query by its ID

## Parameters

- **account_id** (string, required) [path]: Account ID.
- **query_id** (integer, required) [path]: Event query ID

## Response

### 200

Returns the event query.

- **account_id** (integer): Account ID
- **alert_enabled** (boolean): Whether alerts are enabled
- **alert_rollup_enabled** (boolean): Whether alert rollup is enabled
- **created_at** (string): Creation timestamp
- **id** (integer): Unique identifier for the saved query
- **name** (string): Name of the saved query
- **query_json** (string): JSON string containing the query parameters
- **rule_enabled** (boolean): Whether rule is enabled
- **rule_scope** (string): Scope for the rule
- **updated_at** (string): Last update timestamp
- **user_email** (string): Email of the user who created the query

### 404

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
