# Check target connectivity

`PUT /accounts/{account_id}/slurper/target/connectivity-precheck`

Check whether tokens are valid against the target bucket

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **bucket** (string, required): 
- **jurisdiction** (string, optional):  Values: `default`, `eu`, `fedramp`
- **secret** (object, required): 
- **vendor** (string, required):  Values: `r2`

## Response

### 200

Target connectivity checked

_Empty object_

### 4XX

Failure response

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Indicates if the API call was successful or not.
