# Get dataset CSV stream

`GET /radar/datasets/{alias}`

Retrieves the CSV content of a given dataset by alias or ID. When getting the content by alias the latest dataset is returned, optionally filtered by the latest available at a given date.

## Parameters

- **alias** (string, required) [path]: Dataset alias or ID.

## Response

### 200

Successful response.

### 400

Bad request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
