# Create Workers VPC connectivity service

`POST /accounts/{account_id}/connectivity/directory/services`



## Parameters

- **account_id** (string, required) [path]: 

## Request Body

One of: Variant 1

## Response

### 200

Successfully created Workers VPC connectivity service

- **result** (object, optional): 

### 4XX

Failed to create Workers VPC connectivity service

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
