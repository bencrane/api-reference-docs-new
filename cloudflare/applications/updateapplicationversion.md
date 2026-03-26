# Update application version

`PATCH /accounts/{accountId}/resource-library/applications/{id}`

Update application version.

## Parameters

- **accountId** (string, required) [path]: Account ID.
- **id** (string, required) [path]: Application ID.

## Request Body

- **hostnames** (array, optional): Returns the list of hostnames for the application.
- **ip_subnets** (array, optional): Returns the list of IP subnets for the application.
- **port_protocols** (array, optional): Returns the list of port protocols for the application.
- **support_domains** (array, optional): Returns the list of support domains for the application.

## Response

### 200

Update the application response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Indicates whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Update application version response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Indicates whether the API call was successful. Values: `false`
