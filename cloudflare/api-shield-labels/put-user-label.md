# Update user label

`PUT /zones/{zone_id}/api_gateway/labels/user/{name}`

Update all fields on a label

## Request Body

- **description** (string, optional): The description of the label
- **metadata** (object, optional): Metadata for the label

## Response

### 200

Update label response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Update label response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
