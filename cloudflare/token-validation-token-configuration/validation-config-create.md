# Create a new Token Validation configuration

`POST /zones/{zone_id}/token_validation/config`

Create a new Token Validation configuration

## Request Body

- **credentials** (object, required): 
- **description** (string, required): 
- **title** (string, required): 
- **token_sources** (array, required): 
- **token_type** (string, required):  Values: `JWT`

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
