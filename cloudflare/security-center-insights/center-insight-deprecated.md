# Archives Security Center Insight

`PUT /accounts/{account_id}/intel/attack-surface-report/{issue_id}/dismiss`

> **Deprecated**

Deprecated endpoint for archiving Security Center insights. Use the newer archive-security-center-insight endpoint instead.

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
