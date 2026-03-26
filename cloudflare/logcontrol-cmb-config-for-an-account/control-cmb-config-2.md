# Update CMB config

`POST /accounts/{account_id}/logs/control/cmb/config`

Updates CMB config.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **allow_out_of_region_access** (boolean, optional): Allow out of region access
- **regions** (string, optional): Name of the region.

## Response

### 200

Update CMB config response

- **result** (object, optional): 

### 4XX

Update CMB config response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
