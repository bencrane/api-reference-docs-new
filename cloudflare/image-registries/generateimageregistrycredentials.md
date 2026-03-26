# Generate a JWT to interact with the specified image registry.

`POST /accounts/{account_id}/containers/registries/{domain}/credentials`

Generates temporary credentials for accessing Cloudflare's container image registry. Used for pulling and pushing container images.

## Parameters

- **domain** (string, required) [path]: 

## Request Body

- **expiration_minutes** (integer, required): The number of minutes the credentials will be valid for.
- **permissions** (array, required): 

## Response

### 201

Credentials with 'pull' or 'push' permissions to access the registry

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful.
- **result** (object, optional): Credentials that can be used to interact with the requested image registry.

### 400

Bad Request for Public API.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

### 403

The requested token permissions are not allowed for this account

- **error** (string): 

### 404

The image registry does not exist

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

### 409

The registry was configured as public, so credentials can not be generated

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful.

### 500

InternalError500.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
