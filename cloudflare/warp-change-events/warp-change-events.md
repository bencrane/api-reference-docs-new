# List WARP change events.

`GET /accounts/{account_id}/dex/warp-change-events`

List WARP configuration and enablement toggle change events by device.

## Parameters

- **account_id** (string, required) [path]: unique identifier linked to an account in the API request path
- **page** (number, required) [query]: Page number of paginated results
- **per_page** (number, required) [query]: Number of items per page
- **from** (string, required) [query]: Start time for the query in ISO (RFC3339 - ISO 8601) format
- **to** (string, required) [query]: End time for the query in ISO (RFC3339 - ISO 8601) format
- **type** (string, optional) [query]: Filter events by type 'config' or 'toggle'
- **toggle** (string, optional) [query]: Filter events by type toggle value. Applicable to type='toggle' events only.
- **config_name** (string, optional) [query]: Filter events by WARP configuration name changed from or to. Applicable to type='config' events only.
- **account_name** (string, optional) [query]: Filter events by account name.
- **sort_order** (string, optional) [query]: Sort response by event timestamp.

## Response

### 200

success response

- **result** (array, optional): 

### 4XX

List WARP change events failure response

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
