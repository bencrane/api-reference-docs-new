# Create a new TURN key

`POST /accounts/{account_id}/calls/turn_keys`

Creates a new Cloudflare Calls TURN key.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **name** (string, optional): A short description of a TURN key, not shown to end users.

## Response

### 201

Created a new TURN key

- **result** (object, optional):
