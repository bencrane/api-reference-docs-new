# Update Token Configuration credentials

`PUT /zones/{zone_id}/token_validation/config/{config_id}/credentials`

Update Token Configuration credentials

## Request Body

- **keys** (array, required): 

## Response

### 200

OK

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **keys** (array, optional): 

### 4XX

Failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
