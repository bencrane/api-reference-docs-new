# Retrieves Security Center Insights

`GET /accounts/{account_id}/security-center/insights`

Lists all Security Center insights for the account, showing security findings and recommendations.

## Parameters

- **account_id** (string, required) [path]: 
- **dismissed** (string, optional) [query]: 
- **issue_class** (string, optional) [query]: 
- **issue_type** (string, optional) [query]: 
- **product** (string, optional) [query]: 
- **severity** (string, optional) [query]: 
- **subject** (string, optional) [query]: 
- **issue_class~neq** (string, optional) [query]: 
- **issue_type~neq** (string, optional) [query]: 
- **product~neq** (string, optional) [query]: 
- **severity~neq** (string, optional) [query]: 
- **subject~neq** (string, optional) [query]: 
- **page** (string, optional) [query]: 
- **per_page** (string, optional) [query]: 

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
