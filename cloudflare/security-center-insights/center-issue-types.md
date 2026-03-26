# Retrieves Security Center Issues Types

`GET /accounts/{account_id}/intel/attack-surface-report/issue-types`

Lists all available issue types in Security Center, describing categories of security issues.

## Parameters

- **account_id** (string, required) [path]: 

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
