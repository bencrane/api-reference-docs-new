# Preview operations covered by a Token Validation rule

`POST /zones/{zone_id}/token_validation/rules/preview`

Preview operations covered by a Token Validation rule.

The API will return all operations on a zone annotated with an additional `state` field.
Operations with an `included` `state` will be covered by a Token Validation Rule.


## Parameters

- **per_page** (integer, optional) [query]: Maximum number of results per page.
- **page** (integer, optional) [query]: Page number of paginated results.
- **state** (array, optional) [query]: 
- **host** (array, optional) [query]: Filter operations by host.
- **hostname** (array, optional) [query]: Filter operations by host.
- **method** (array, optional) [query]: Filter operations by method.
- **endpoint** (array, optional) [query]: Filter operations by endpoint. Allows substring matching.

## Request Body

- **exclude** (array, optional): Ignore operations that were otherwise included by `include`.
- **include** (array, optional): Select all matching operations.

## Response

### 200

OK

- **result** (object, optional): 

### 4XX

Failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
