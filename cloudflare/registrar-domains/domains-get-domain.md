# Get domain

`GET /accounts/{account_id}/registrar/domains/{domain_name}`

Show individual domain.

## Parameters

- **domain_name** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Get domain response

- **result** (object, optional): 

### 4XX

Get domain response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
