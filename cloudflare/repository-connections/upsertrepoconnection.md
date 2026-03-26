# Create or update repository connection

`PUT /accounts/{account_id}/builds/repos/connections`

Upsert a repository connection for CI/CD integration

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **provider_account_id** (string, required): Provider account identifier.
- **provider_account_name** (string, required): 
- **provider_type** (string, required):  Values: `github`
- **repo_id** (string, required): Repository identifier.
- **repo_name** (string, required): 

## Response

### 200

Repository connection upserted successfully

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): 
- **result_info** (object, optional): 
- **success** (boolean, optional):
