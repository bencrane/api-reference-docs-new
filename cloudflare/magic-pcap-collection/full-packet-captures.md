# Add buckets for full packet captures

`POST /accounts/{account_id}/pcaps/ownership`

Adds an AWS or GCP bucket to use with full packet captures.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **destination_conf** (string, required): The full URI for the bucket. This field only applies to `full` packet captures.

## Response

### 200

Add buckets for full packet captures response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`

### default

Add buckets for full packet captures response failure.

Type: object
