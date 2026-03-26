# Return WebVTT captions for a provided language

`GET /accounts/{account_id}/stream/{identifier}/captions/{language}/vtt`

Return WebVTT captions for a provided language.

## Parameters

- **language** (string, required) [path]: 
- **identifier** (string, required) [path]: 
- **account_id** (string, required) [path]: 


## Response

### 200

Return WebVTT caption or subtitle response.

### 4XX

Return WebVTT caption or subtitle response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
