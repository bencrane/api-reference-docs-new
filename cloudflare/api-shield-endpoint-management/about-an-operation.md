# Retrieve information about an operation

`GET /zones/{zone_id}/api_gateway/operations/{operation_id}`

Gets detailed information about a specific API operation in API Shield, including its schema validation settings and traffic statistics.

## Parameters

- **feature** (array, optional) [query]: Add feature(s) to the results. The feature name that is given here corresponds to the resulting feature object. Have a look at the top-level object description for more details on the specific meaning.

## Response

### 200

Retrieve information about an operation response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Retrieve information about an operation response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
