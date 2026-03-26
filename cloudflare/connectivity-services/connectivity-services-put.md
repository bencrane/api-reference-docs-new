# Update Workers VPC connectivity service

`PUT /accounts/{account_id}/connectivity/directory/services/{service_id}`



## Parameters

- **account_id** (string, required) [path]: 
- **service_id** (string, required) [path]: 

## Request Body

One of: Variant 1

## Response

### 200

Successfully updated Workers VPC connectivity service

- **result** (object, optional): 

### 4XX

Failed to update Workers VPC connectivity service

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
