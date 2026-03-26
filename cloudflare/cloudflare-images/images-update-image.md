# Update image

`PATCH /accounts/{account_id}/images/v1/{image_id}`

Update image access control. On access control change, all copies of the image are purged from cache.

## Parameters

- **image_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

- **creator** (string, optional): Can set the creator field with an internal user ID.
- **metadata** (object, optional): User modifiable key-value store. Can be used for keeping references to another system of record for managing images. No change if not specified.
- **requireSignedURLs** (boolean, optional): Indicates whether the image can be accessed using only its UID. If set to `true`, a signed token needs to be generated with a signing key to view the image. Returns a new UID on a change. No change if not specified.

## Response

### 200

Update image response

- **result** (object, optional): 

### 4XX

Update image response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
