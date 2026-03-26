# Reads an indicator

`GET /accounts/{account_id}/cloudforce-one/events/dataset/{dataset_id}/indicators/{indicator_id}`

Retrieves a specific indicator by its UUID.

## Parameters

- **account_id** (string, required) [path]: Account ID.
- **dataset_id** (string, required) [path]: Dataset ID.
- **indicator_id** (string, required) [path]: Indicator UUID.

## Response

### 200

Returns the indicator.

- **createdAt** (string): 
- **datasetId** (string): The dataset ID this indicator belongs to. Included in list responses.
- **indicatorType** (string): 
- **relatedEvents** (array): 
- **tags** (array): 
- **updatedAt** (string): 
- **uuid** (string): 
- **value** (string): 

### 404

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
