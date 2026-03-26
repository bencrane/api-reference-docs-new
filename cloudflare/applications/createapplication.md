# Create application

`POST /accounts/{accountId}/resource-library/applications`

Create application.

## Parameters

- **accountId** (string, required) [path]: Account ID.

## Request Body

- **application_type_id** (string, required): Provide as string to perform a lookup to check if the source exists.
- **hostnames** (object, optional): 
- **human_id** (string, required): Returns the human readable ID.
- **ip_subnets** (array, optional): Returns the list of IP subnets for the application.
- **name** (string, required): Returns the application name.
- **port_protocols** (array, optional): Returns the list of port protocols for the application.
- **support_domains** (array, optional): Returns the list of support domains for the application.

## Response

### 201

Created.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Indicates whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Create application response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Indicates whether the API call was successful. Values: `false`
