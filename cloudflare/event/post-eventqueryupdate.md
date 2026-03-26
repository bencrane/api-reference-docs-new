# Update a saved event query

`POST /accounts/{account_id}/cloudforce-one/events/queries/{query_id}`

Update an existing saved event query by its ID

## Parameters

- **account_id** (string, required) [path]: Account ID.
- **query_id** (integer, required) [path]: Event query ID

## Request Body

- **alert_enabled** (boolean, optional): Enable alerts for this query
- **alert_rollup_enabled** (boolean, optional): Enable alert rollup for this query
- **name** (string, optional): Unique name for the saved query
- **query_json** (string, optional): JSON string containing the query parameters
- **rule_enabled** (boolean, optional): Enable rule for this query
- **rule_scope** (string, optional): Scope for the rule

## Response

### 200

Returns the updated event query.

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

### 400

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean): 

### 404

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
