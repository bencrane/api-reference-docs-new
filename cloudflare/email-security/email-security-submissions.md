# Get reclassify submissions

`GET /accounts/{account_id}/email-security/submissions`

This endpoint returns information for submissions to made to reclassify emails.

## Parameters

- **account_id** (string, required) [path]: 
- **start** (string, optional) [query]: The beginning of the search date range.
Defaults to `now - 30 days` if not provided.
- **end** (string, optional) [query]: The end of the search date range.
Defaults to `now` if not provided.
- **type** (string, optional) [query]: 
- **submission_id** (string, optional) [query]: 
- **original_disposition** (string, optional) [query]: 
- **requested_disposition** (string, optional) [query]: 
- **outcome_disposition** (string, optional) [query]: 
- **status** (string, optional) [query]: 
- **query** (string, optional) [query]: 
- **customer_status** (string, optional) [query]: 
- **page** (integer, optional) [query]: The page number of paginated results.
- **per_page** (integer, optional) [query]: The number of results per page.

## Response

### 200



- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): 
- **result** (array, optional): 
- **result_info** (object, optional): 

### 4XX

Client Error

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean):
