# Patch user label

`PATCH /zones/{zone_id}/api_gateway/labels/user/{name}`

Update certain fields on a label

## Request Body

- **description** (string, optional): The description of the label
- **metadata** (object, optional): Metadata for the label

## Response

### 200

Patch label response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Patch label response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
