# Retrieve user label

`GET /zones/{zone_id}/api_gateway/labels/user/{name}`

Retrieve user label

## Parameters

- **with_mapped_resource_counts** (boolean, optional) [query]: Include `mapped_resources` for each label

## Response

### 200

Retrieve user label response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Retrieve user label response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
