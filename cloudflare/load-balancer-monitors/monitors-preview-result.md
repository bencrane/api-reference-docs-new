# Preview Result

`GET /user/load_balancers/preview/{preview_id}`

Get the result of a previous preview operation using the provided preview_id.

## Parameters

- **preview_id** (string, required) [path]: 

## Response

### 200

Preview Result response.

- **result** (object, optional): Resulting health data from a preview operation.

### 4XX

Preview Result response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
