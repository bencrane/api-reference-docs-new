# Get account audit logs

`GET /accounts/{account_id}/audit_logs`

Gets a list of audit logs for an account. Can be filtered by who made the change, on which zone, and the timeframe of the change.

## Parameters

- **account_id** (string, required) [path]: 
- **id** (string, optional) [query]: 
- **export** (boolean, optional) [query]: 
- **action.type** (string, optional) [query]: 
- **actor.ip** (string, optional) [query]: 
- **actor.email** (string, optional) [query]: 
- **since** (string, optional) [query]: 
- **before** (string, optional) [query]: 
- **zone.name** (string, optional) [query]: 
- **direction** (string, optional) [query]: 
- **per_page** (number, optional) [query]: 
- **page** (number, optional) [query]: 
- **hide_user_logs** (boolean, optional) [query]: 

## Response

### 200

Get account audit logs response

Type: object

### 4XX

Get account audit logs response failure

- **errors** (object, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `false`
