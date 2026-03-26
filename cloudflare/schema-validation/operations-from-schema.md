# Retrieve all operations from the schema.

`GET /zones/{zone_id}/schema_validation/schemas/{schema_id}/operations`

Retrieves all operations from the schema. Operations that already exist in API Shield Endpoint Management will be returned as full operations.

## Parameters

- **feature** (array, optional) [query]: Add feature(s) to the results. The feature name that is given here corresponds to the resulting feature object. Have a look at the top-level object description for more details on the specific meaning.
- **host** (array, optional) [query]: 
- **method** (array, optional) [query]: 
- **endpoint** (string, optional) [query]: 
- **page** (integer, optional) [query]: Page number of paginated results.
- **per_page** (integer, optional) [query]: Maximum number of results per page.
- **operation_status** (string, optional) [query]: Filter results by whether operations exist in Web Asset Management or not. `new` will just return operations from the schema that do not exist otherwise. `existing` will just return operations from the schema that already exist.

## Response

### 200

All operations in the schema

_Empty object_

### 4XX

Failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
