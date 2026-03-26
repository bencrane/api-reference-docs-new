# Updates an indicator

`PATCH /accounts/{account_id}/cloudforce-one/events/dataset/{dataset_id}/indicators/{indicator_id}`

Updates an existing indicator's properties.

## Parameters

- **account_id** (string, required) [path]: Account ID.
- **dataset_id** (string, required) [path]: Dataset ID.
- **indicator_id** (string, required) [path]: Indicator UUID.

## Request Body

- **indicatorType** (string, optional): 
- **relatedEvents** (array, optional): 
- **tags** (array, optional): 
- **value** (string, optional): 

## Response

### 200

Returns the updated indicator.

- **createdAt** (string): 
- **datasetId** (string): The dataset ID this indicator belongs to. Included in list responses.
- **indicatorType** (string): 
- **relatedEvents** (array): 
- **tags** (array): 
- **updatedAt** (string): 
- **uuid** (string): 
- **value** (string): 

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
