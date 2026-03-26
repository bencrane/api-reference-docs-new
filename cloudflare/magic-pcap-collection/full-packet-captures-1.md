# Validate buckets for full packet captures

`POST /accounts/{account_id}/pcaps/ownership/validate`

Validates buckets added to the packet captures API.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **destination_conf** (string, required): The full URI for the bucket. This field only applies to `full` packet captures.
- **ownership_challenge** (string, required): The ownership challenge filename stored in the bucket.

## Response

### 200

Validate buckets for full packet captures response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`

### default

Validate buckets for full packet captures response failure.

Type: object
