# List Placement Regions

`GET /accounts/{account_id}/workers/placement/regions`

Returns a list of available placement regions organized by cloud provider. These regions can be used to configure Smart Placement for Workers.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

List Placement Regions response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

List Placement Regions response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
