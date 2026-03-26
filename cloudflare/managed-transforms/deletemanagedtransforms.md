# Delete Managed Transforms

`DELETE /zones/{zone_id}/managed_headers`

Disables all Managed Transforms.

## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 204

An empty response.

### 4XX

A failure response.

- **errors** (array, optional): A list of error messages.
- **messages** (array, optional): A list of warning messages.
- **result** (enum, optional):  Values: ``
- **success** (enum, optional):  Values: `false`
