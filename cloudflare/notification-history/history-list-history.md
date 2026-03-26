# List History

`GET /accounts/{account_id}/alerting/v3/history`

Gets a list of history records for notifications sent to an account. The records are displayed for last `x` number of days based on the zone plan (free = 30, pro = 30, biz = 30, ent = 90).

## Parameters

- **account_id** (string, required) [path]: 
- **per_page** (string, optional) [query]: 
- **before** (string, optional) [query]: 
- **page** (number, optional) [query]: 
- **since** (string, optional) [query]: 

## Response

### 200

List History response

- **result** (array, optional): 
- **result_info** (object, optional): 

### 4XX

List History response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `false`
