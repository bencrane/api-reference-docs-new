# Generate authentication token for VPC flow logs export.

`POST /accounts/{account_id}/mnm/vpc-flows/token`

Generate authentication token for VPC flow logs export.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

Generate authentication token for VPC flow logs export response.

- **result** (string, optional): Authentication token to be used for VPC Flows export authentication.

### 4XX

Generate authentication token for VPC flow logs export failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
