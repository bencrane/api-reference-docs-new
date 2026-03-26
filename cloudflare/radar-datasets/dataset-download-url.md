# Get dataset download URL

`POST /radar/datasets/download`

Retrieves an URL to download a single dataset.

## Parameters

- **format** (string, optional) [query]: Format in which results will be returned.

## Request Body

- **datasetId** (integer, required): 

## Response

### 200

Successful response.

- **result** (object): 

### 400

Bad request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
