# Get bulk operation status

`GET /accounts/{account_id}/rules/lists/bulk_operations/{operation_id}`

Gets the current status of an asynchronous operation on a list.

The `status` property can have one of the following values: `pending`, `running`, `completed`, or `failed`. If the status is `failed`, the `error` property will contain a message describing the error.

## Parameters

- **operation_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Get bulk operation status response.

- **result** (object, optional): 
- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Defines whether the API call was successful. Values: `true`

### 4XX

Get bulk operation status response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
