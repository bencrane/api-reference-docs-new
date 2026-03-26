# Create build token

`POST /accounts/{account_id}/builds/tokens`

Create a new build authentication token

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **build_token_name** (string, required): 
- **build_token_secret** (string, required): 
- **cloudflare_token_id** (string, required): 

## Response

### 200

Build token created successfully

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): 
- **result_info** (object, optional): 
- **success** (boolean, optional):
