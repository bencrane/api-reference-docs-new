# Variant details (flat)

`GET /accounts/{account_id}/images/v1/variants/{variant_id}/flat`

Fetch details for a single variant with properties at the top level of the result.

## Parameters

- **variant_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Variant details flat response

- **result** (object, optional): 

### 4XX

Variant details flat response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
