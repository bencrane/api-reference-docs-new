# List indicators related to a tag

`GET /accounts/{account_id}/cloudforce-one/events/dataset/{dataset_id}/tags/{tag_uuid}/indicators`

Returns indicators associated with the provided tag UUID across all indicator datasets, with pagination.

## Parameters

- **account_id** (string, required) [path]: Account ID.
- **tag_uuid** (string, required) [path]: Tag UUID.
- **dataset_id** (string, required) [path]: Dataset UUID.
- **page** (number, optional) [query]: 
- **pageSize** (number, optional) [query]: 
- **indicatorType** (string, optional) [query]: 
- **relatedEvent** (array, optional) [query]: Filter indicators by related event UUID(s). Multiple UUIDs can be provided by repeating the parameter.

## Response

### 200

Returns a paginated list of indicators.

- **indicators** (array): 
- **pagination** (object): 

### 400

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean): 

### 404

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean): 

### 500

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
