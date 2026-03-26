# List fleet status details by dimension

`GET /accounts/{account_id}/dex/fleet-status/live`

List details for live (up to 60 minutes) devices using WARP

## Parameters

- **account_id** (string, required) [path]: Unique identifier for account
- **since_minutes** (string, required) [query]: Number of minutes before current time

## Response

### 200

List device details (live) response

- **result** (object, optional): 

### 4XX

List device details (live) response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
