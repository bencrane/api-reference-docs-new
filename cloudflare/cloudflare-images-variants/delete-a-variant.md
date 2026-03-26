# Delete a variant

`DELETE /accounts/{account_id}/images/v1/variants/{variant_id}`

Deleting a variant purges the cache for all images associated with the variant.

## Parameters

- **variant_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 


## Response

### 200

Delete a variant response

- **result** (object, optional): 

### 4XX

Delete a variant response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
