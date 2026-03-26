# Archives Security Center Insight

`PUT /accounts/{account_id}/security-center/insights/{issue_id}/dismiss`

Archives a Security Center insight for an account, removing it from the active insights list while preserving historical data.

## Parameters

- **account_id** (string, required) [path]: 
- **issue_id** (string, required) [path]: 

## Request Body

- **dismiss** (boolean, optional): 

## Response

### 200

The request was successful.

_Empty object_

### 4XX

A client error occurred.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
