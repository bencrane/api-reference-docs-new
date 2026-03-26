# Get Workers VPC connectivity service

`GET /accounts/{account_id}/connectivity/directory/services/{service_id}`



## Parameters

- **account_id** (string, required) [path]: 
- **service_id** (string, required) [path]: 

## Response

### 200

Successfully retrieved Workers VPC connectivity service

- **result** (object, optional): 

### 4XX

Failed to retrieve Workers VPC connectivity service

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
