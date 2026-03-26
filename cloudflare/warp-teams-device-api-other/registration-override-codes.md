# Get override codes

`GET /accounts/{account_id}/devices/registrations/{registration_id}/override_codes`

Fetches one-time use admin override codes for a registration. This relies on the **Admin Override** setting being enabled in your device configuration.

## Parameters

- **account_id** (string, required) [path]: 
- **registration_id** (string, required) [path]: 

## Response

### 200

Get admin override codes for a registration response.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
