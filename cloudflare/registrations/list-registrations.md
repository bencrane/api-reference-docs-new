# List registrations

`GET /accounts/{account_id}/devices/registrations`

Lists WARP registrations.

## Parameters

- **account_id** (string, required) [path]: 
- **user.id** (array, optional) [query]: Filter by user ID.
- **seen_after** (string, optional) [query]: Filter by the last_seen timestamp - returns only registrations last seen after this timestamp.
- **seen_before** (string, optional) [query]: Filter by the last_seen timestamp - returns only registrations last seen before this timestamp.
- **status** (string, optional) [query]: Filter by registration status. Defaults to 'active'.
- **per_page** (integer, optional) [query]: The maximum number of devices to return in a single response.
- **search** (string, optional) [query]: Filter by registration details.
- **sort_by** (string, optional) [query]: The registration field to order results by.
- **sort_order** (string, optional) [query]: Sort direction.
- **cursor** (string, optional) [query]: Opaque token indicating the starting position when requesting the next set of records. A cursor value can be obtained from the result_info.cursor field in the response.
- **id** (array, optional) [query]: Filter by registration ID.
- **device.id** (string, optional) [query]: Filter by WARP device ID.
- **include** (string, optional) [query]: Comma-separated list of additional information that should be included in the registration response. Supported values are: "policy".


## Response

### 200

List of registrations response.

- **errors** (array): 
- **messages** (array): 
- **result** (array): 
- **result_info** (object): V4 public API Pagination/Cursor info.
- **success** (boolean): Whether the API call was successful.
