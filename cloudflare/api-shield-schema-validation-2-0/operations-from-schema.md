# Retrieve all operations from a schema.

`GET /zones/{zone_id}/api_gateway/user_schemas/{schema_id}/operations`

> **Deprecated**

Retrieves all operations from the schema. Operations that already exist in API Shield Endpoint Management will be returned as full operations.

## Parameters

- **feature** (array, optional) [query]: Add feature(s) to the results. The feature name that is given here corresponds to the resulting feature object. Have a look at the top-level object description for more details on the specific meaning.
- **host** (array, optional) [query]: 
- **method** (array, optional) [query]: 
- **endpoint** (string, optional) [query]: 
- **page** (integer, optional) [query]: Page number of paginated results.
- **per_page** (integer, optional) [query]: Maximum number of results per page.
- **operation_status** (string, optional) [query]: Filter results by whether operations exist in API Shield Endpoint Management or not. `new` will just return operations from the schema that do not exist in API Shield Endpoint Management. `existing` will just return operations from the schema that already exist in API Shield Endpoint Management.

## Response

### 200

Retrieve all operations from a schema response

- **result** (array, optional): 

### 4XX

Retrieve all operations from a schema response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
