# List Workers

`GET /accounts/{account_id}/workers/scripts`

Fetch a list of uploaded workers.

## Parameters

- **account_id** (string, required) [path]: 
- **tags** (string, optional) [query]: Filter scripts by tags. Format: comma-separated list of tag:allowed pairs where allowed is 'yes' or 'no'.

## Response

### 200

List Workers response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (array, optional): 

### 4XX

List Workers response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
