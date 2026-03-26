# Get ownership challenge

`POST /zones/{zone_id}/logpush/ownership`

Gets a new ownership challenge sent to your destination.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **destination_conf** (string, required): Uniquely identifies a resource (such as an s3 bucket) where data. will be pushed. Additional configuration parameters supported by the destination may be included.

## Response

### 200

Get ownership challenge response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Get ownership challenge response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
