# Create an event query alert

`POST /accounts/{account_id}/cloudforce-one/events/queries/alerts/create`

Create a new alert subscription for an event query

## Parameters

- **account_id** (string, required) [path]: Account ID.

## Request Body

- **enabled** (boolean, optional): Whether the alert is enabled
- **frequency** (string, optional): Alert frequency (immediate or daily) Values: `immediate`, `daily`
- **notification_type** (string, optional): Type of notification (e.g., ans)
- **query_id** (integer, required): ID of the event query to create an alert for

## Response

### 200

Returns the created event query alert.

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
