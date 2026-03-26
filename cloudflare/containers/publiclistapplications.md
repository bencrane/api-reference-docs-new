# List containers.

`GET /accounts/{account_id}/containers`

Lists all the container applications that are associated with your account.

## Parameters

- **name** (string, optional) [query]: Filter containers by name
- **image** (string, optional) [query]: Filter containers by image

## Response

### 200

Returns all public applications associated with your account.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful.
- **result** (array, optional): 

### 401

Unauthorized for Public API.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

### 500

InternalError500.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
