# Retrieve operations and features as OpenAPI schemas

`GET /zones/{zone_id}/api_gateway/schemas`



## Parameters

- **host** (array, optional) [query]: 
- **feature** (array, optional) [query]: Add feature(s) to the results. The feature name that is given here corresponds to the resulting feature object. Have a look at the top-level object description for more details on the specific meaning.

## Response

### 200

Retrieve operations and features as OpenAPI schemas response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Retrieve operations and features as OpenAPI schemas response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
