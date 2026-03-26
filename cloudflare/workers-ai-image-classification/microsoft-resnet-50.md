# Execute @cf/microsoft/resnet-50 model.

`POST /accounts/{account_id}/ai/run/@cf/microsoft/resnet-50`

Runs inference on the @cf/microsoft/resnet-50 model.

## Parameters

- **account_id** (string, required) [path]: 
- **queueRequest** (string, optional) [query]: 
- **tags** (string, optional) [query]: 


## Response

### 200

Object with user data.

Type: object

### 400

Bad request

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
