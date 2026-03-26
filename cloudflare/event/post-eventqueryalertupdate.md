# Update an event query alert

`POST /accounts/{account_id}/cloudforce-one/events/queries/alerts/{alert_id}`

Update an existing event query alert by its ID

## Parameters

- **account_id** (string, required) [path]: Account ID.
- **alert_id** (integer, required) [path]: Event query alert ID

## Request Body

- **enabled** (boolean, optional): Whether the alert is enabled
- **frequency** (string, optional): Alert frequency (immediate or daily) Values: `immediate`, `daily`
- **notification_type** (string, optional): Type of notification (e.g., ans)

## Response

### 200

Returns the updated event query alert.

- **account_id** (integer): Account ID
- **created_at** (string): Creation timestamp
- **enabled** (boolean): Whether the alert is enabled
- **frequency** (string): Alert frequency (immediate or daily)
- **id** (integer): Unique identifier for the event query alert
- **last_sent_at** (string): Last time the alert was sent
- **notification_type** (string): Type of notification
- **query_id** (integer): ID of the associated event query
- **updated_at** (string): Last update timestamp
- **user_email** (string): Email of the user who created the alert

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
