# Validate destination

`POST /accounts/{account_id}/logpush/validate/destination`

Validates destination.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **destination_conf** (string, required): Uniquely identifies a resource (such as an s3 bucket) where data. will be pushed. Additional configuration parameters supported by the destination may be included.

## Response

### 200

Validate destination response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Validate destination response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
