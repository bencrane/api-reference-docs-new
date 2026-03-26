# List interconnect Details

`GET /accounts/{account_id}/magic/cf_interconnects/{cf_interconnect_id}`

Lists details for a specific interconnect.

## Parameters

- **cf_interconnect_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 
- **x-magic-new-hc-target** (boolean, optional) [header]: If true, the health check target in the response body will be presented using the new object format. Defaults to false.

## Response

### 200

List interconnect Details response

- **result** (object, optional): 

### 4XX

List interconnect Details response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
