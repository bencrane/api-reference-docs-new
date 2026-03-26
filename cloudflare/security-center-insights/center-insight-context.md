# Retrieves Security Center Insight Context

`GET /accounts/{account_id}/security-center/insights/{issue_id}/context`

Returns the full context payload for an insight. This endpoint is used for insights with large payloads that are not included inline in the list response.

## Parameters

- **account_id** (string, required) [path]: 
- **issue_id** (string, required) [path]: 

## Response

### 200

The request was successful.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

A client error occurred.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
