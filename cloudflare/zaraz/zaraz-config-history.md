# Get Zaraz historical configurations by ID(s)

`GET /zones/{zone_id}/settings/zaraz/history/configs`

Gets a history of published Zaraz configurations by ID(s) for a zone.

## Parameters

- **zone_id** (string, required) [path]: 
- **ids** (array, required) [query]: Comma separated list of Zaraz configuration IDs.

## Response

### 200

Get Zaraz historical configurations by ID(s) response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful.
- **result** (object, optional): Object where keys are numeric configuration IDs.

### 4XX

Get Zaraz historical configurations by ID(s) failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
