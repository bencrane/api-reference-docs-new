# Creates a new indicator

`POST /accounts/{account_id}/cloudforce-one/events/dataset/{dataset_id}/indicators/create`

Creates a new indicator with the specified type and related datasets.

## Parameters

- **account_id** (string, required) [path]: Account ID.
- **dataset_id** (string, required) [path]: Dataset UUID.

## Request Body

- **autoCreateType** (boolean, optional): If true, automatically create the indicator type if it doesn't exist. If false (default), throw an error when the indicator type doesn't exist.
- **indicatorType** (string, required): 
- **relatedEvents** (array, optional): 
- **tags** (array, optional): 
- **value** (string, required): 

## Response

### 200

Returns the created indicator.

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
