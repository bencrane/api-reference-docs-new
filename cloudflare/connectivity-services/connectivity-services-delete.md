# Delete Workers VPC connectivity service

`DELETE /accounts/{account_id}/connectivity/directory/services/{service_id}`



## Parameters

- **account_id** (string, required) [path]: 
- **service_id** (string, required) [path]: 

## Response

### 200

Successfully deleted Workers VPC connectivity service

### 4XX

Failed to delete Workers VPC connectivity service

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
