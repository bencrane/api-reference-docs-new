# Retrieves countries information for all countries

`GET /accounts/{account_id}/cloudforce-one/events/countries`



## Parameters

- **account_id** (string, required) [path]: Account ID.

## Response

### 200

Returns the long and short country code for every country.

Type: array

### 400

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
