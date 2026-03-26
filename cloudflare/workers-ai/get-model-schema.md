# Get Model Schema

`GET /accounts/{account_id}/ai/models/schema`

Retrieves the input and output JSON schema definition for a Workers AI model.

## Parameters

- **account_id** (string, required) [path]: 
- **model** (string, required) [query]: Model Name

## Response

### 200

Model Schema

- **result** (object): 
- **success** (boolean): 

### 400

Bad Request

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
