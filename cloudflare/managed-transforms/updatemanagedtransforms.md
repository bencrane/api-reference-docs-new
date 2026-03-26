# Update Managed Transforms

`PATCH /zones/{zone_id}/managed_headers`

Updates the status of one or more Managed Transforms.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **managed_request_headers** (array, required): The list of Managed Request Transforms.
- **managed_response_headers** (array, required): The list of Managed Response Transforms.

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
