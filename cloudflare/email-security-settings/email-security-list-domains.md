# List protected email domains

`GET /accounts/{account_id}/email-security/settings/domains`

Lists, searches, and sorts an account’s email domains.

## Parameters

- **account_id** (string, required) [path]: 
- **page** (integer, optional) [query]: The page number of paginated results.
- **per_page** (integer, optional) [query]: The number of results per page.
- **order** (string, optional) [query]: The field to sort by.
- **direction** (string, optional) [query]: The sorting direction.
- **search** (string, optional) [query]: Allows searching in multiple properties of a record simultaneously.
This parameter is intended for human users, not automation. Its exact
behavior is intentionally left unspecified and is subject to change
in the future.
- **allowed_delivery_mode** (string, optional) [query]: Filters response to domains with the provided delivery mode.
- **domain** (array, optional) [query]: Filters results by the provided domains, allowing for multiple occurrences.
- **active_delivery_mode** (string, optional) [query]: Filters response to domains with the currently active delivery mode.
- **integration_id** (string, optional) [query]: Filters response to domains with the provided integration ID.

## Response

### 200

Contains a list of domains for the account.

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
