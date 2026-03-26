# Execute @cf/moonshotai/kimi-k2.5 model.

`POST /accounts/{account_id}/ai/run/@cf/moonshotai/kimi-k2.5`

Runs inference on the @cf/moonshotai/kimi-k2.5 model.

## Parameters

- **account_id** (string, required) [path]: 
- **queueRequest** (string, optional) [query]: 
- **tags** (string, optional) [query]: 

## Request Body

One of: object, object

## Response

### 200

Object with user data.

Type: object

### 400

Bad request

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
