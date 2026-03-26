# Retrieve managed label

`GET /zones/{zone_id}/api_gateway/labels/managed/{name}`

Retrieve managed label

## Parameters

- **with_mapped_resource_counts** (boolean, optional) [query]: Include `mapped_resources` for each label

## Response

### 200

Retrieve managed label response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Retrieve managed label response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
