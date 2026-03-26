# List Workers VPC connectivity services

`GET /accounts/{account_id}/connectivity/directory/services`



## Parameters

- **account_id** (string, required) [path]: 
- **type** (string, optional) [query]: 
- **page** (integer, optional) [query]: Current page in the response
- **per_page** (integer, optional) [query]: Max amount of entries returned per page

## Response

### 200

Successfully retrieved Workers VPC connectivity services

- **result** (array, optional): 

### 4XX

Failed to retrieve Workers VPC connectivity services

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
