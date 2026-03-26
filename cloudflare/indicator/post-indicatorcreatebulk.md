# Creates multiple indicators in bulk

`POST /accounts/{account_id}/cloudforce-one/events/dataset/{dataset_id}/indicators/bulk`

Creates multiple indicators at once with their respective types and related datasets.

## Parameters

- **account_id** (string, required) [path]: Account ID.
- **dataset_id** (string, required) [path]: Dataset UUID.

## Request Body

- **autoCreateType** (boolean, optional): Global flag to automatically create indicator types if they don't exist. Individual indicators can override this with their own autoCreateType flag.
- **indicators** (array, required): 

## Response

### 200

Returns the number of created indicators.

Type: number

### 400

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
