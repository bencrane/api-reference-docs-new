# List watermark profiles

`GET /accounts/{account_id}/stream/watermarks`

Lists all watermark profiles for an account.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

List watermark profiles response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (array, optional): 

### 4XX

List watermark profiles response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
