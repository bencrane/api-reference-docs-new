# Check source connectivity

`PUT /accounts/{account_id}/slurper/source/connectivity-precheck`

Check whether tokens are valid against the source bucket

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

_Empty object_

## Response

### 200

Source connectivity checked

_Empty object_

### 4XX

Failure response

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Indicates if the API call was successful or not.
