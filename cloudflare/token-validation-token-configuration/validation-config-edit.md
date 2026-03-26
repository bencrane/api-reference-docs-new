# Edit an existing Token Configuration

`PATCH /zones/{zone_id}/token_validation/config/{config_id}`

Edit fields of an existing Token Configuration

## Request Body

- **description** (string, optional): 
- **title** (string, optional): 
- **token_sources** (array, optional): 

## Response

### 200

OK

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
