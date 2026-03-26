# Delete watermark profiles

`DELETE /accounts/{account_id}/stream/watermarks/{identifier}`

Deletes a watermark profile.

## Parameters

- **identifier** (string, required) [path]: 
- **account_id** (string, required) [path]: 


## Response

### 200

Delete watermark profiles response.

- **result** (string, optional): 

### 4XX

Delete watermark profiles response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
