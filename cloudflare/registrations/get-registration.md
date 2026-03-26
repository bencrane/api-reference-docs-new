# Get registration

`GET /accounts/{account_id}/devices/registrations/{registration_id}`

Fetches a single WARP registration.

## Parameters

- **registration_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 
- **include** (string, optional) [query]: Comma-separated list of additional information that should be included in the registration response. Supported values are: "policy".


## Response

### 200

Returns a Registration.

- **errors** (array): 
- **messages** (array): 
- **result** (object): A WARP configuration tied to a single user. Multiple registrations can be created from a single WARP device.
- **success** (boolean): Whether the API call was successful.
