# List devices

`GET /accounts/{account_id}/devices/physical-devices`

Lists WARP devices.

## Parameters

- **account_id** (string, required) [path]: 
- **cursor** (string, optional) [query]: Opaque token indicating the starting position when requesting the next set of records. A cursor value can be obtained from the result_info.cursor field in the response.
- **sort_by** (string, optional) [query]: The device field to order results by.
- **sort_order** (string, optional) [query]: Sort direction.
- **last_seen_user.email** (string, optional) [query]: Filter by the last seen user's email.
- **seen_after** (string, optional) [query]: Filter by the last_seen timestamp - returns only devices last seen after this timestamp.
- **seen_before** (string, optional) [query]: Filter by the last_seen timestamp - returns only devices last seen before this timestamp.
- **per_page** (integer, optional) [query]: The maximum number of devices to return in a single response.
- **search** (string, optional) [query]: Search by device details.
- **active_registrations** (string, optional) [query]: Include or exclude devices with active registrations. The default is "only" - return only devices with active registrations.
- **id** (array, optional) [query]: Filter by a one or more device IDs.
- **include** (string, optional) [query]: Comma-separated list of additional information that should be included in the device response. Supported values are: "last_seen_registration.policy".


## Response

### 200

Returns a list of Devices.

- **errors** (array): 
- **messages** (array): 
- **result** (array): 
- **result_info** (object): V4 public API Pagination/Cursor info.
- **success** (boolean): Whether the API call was successful.
