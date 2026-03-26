# List Managed Transforms

`GET /zones/{zone_id}/managed_headers`

Fetches a list of all Managed Transforms.

## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 200

A Managed Transforms response.

- **errors** (enum, optional):  Values: ``
- **messages** (array, optional): A list of warning messages.
- **result** (object, optional): A Managed Transforms object.
- **success** (enum, optional):  Values: `true`

### 4XX

A failure response.

- **errors** (array, optional): A list of error messages.
- **messages** (array, optional): A list of warning messages.
- **result** (enum, optional):  Values: ``
- **success** (enum, optional):  Values: `false`
