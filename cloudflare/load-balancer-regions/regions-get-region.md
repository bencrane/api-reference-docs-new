# Get Region

`GET /accounts/{account_id}/load_balancers/regions/{region_id}`

Get a single region mapping.

## Parameters

- **region_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Get Region response.

- **result** (object, optional): A list of countries and subdivisions mapped to a region.

### 4XX

Get Region response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
