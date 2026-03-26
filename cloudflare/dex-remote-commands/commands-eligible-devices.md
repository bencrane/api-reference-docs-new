# List devices eligible for remote captures

`GET /accounts/{account_id}/dex/commands/devices`

List devices with WARP client support for remote captures which have been connected in the last 1 hour.

## Parameters

- **account_id** (string, required) [path]: unique identifier linked to an account in the API request path
- **page** (number, required) [query]: Page number of paginated results
- **per_page** (number, required) [query]: Number of items per page
- **search** (string, optional) [query]: Filter devices by name or email

## Response

### 200

List of eligible devices

- **result** (object, optional): 

### 4XX

List eligible devices failure response

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
