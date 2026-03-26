# Get organization accounts

`GET /organizations/{organization_id}/accounts`

Retrieve a list of accounts that belong to a specific organization. (Currently in Closed Beta - see https://developers.cloudflare.com/fundamentals/organizations/)

## Parameters

- **organization_id** (string, required) [path]: The ID of the organization to retrieve a list of accounts for.
- **account_pubname** (string, optional) [query]: (case-insensitive) Filter the list of accounts to where the account_pubname is equal to
a particular string.
- **account_pubname.startsWith** (string, optional) [query]: (case-insensitive) Filter the list of accounts to where the account_pubname starts with
a particular string.
- **account_pubname.endsWith** (string, optional) [query]: (case-insensitive) Filter the list of accounts to where the account_pubname ends with
a particular string.
- **account_pubname.contains** (string, optional) [query]: (case-insensitive) Filter the list of accounts to where the account_pubname contains
a particular string.
- **name** (string, optional) [query]: (case-insensitive) Filter the list of accounts to where the name is equal to a
particular string.
- **name.startsWith** (string, optional) [query]: (case-insensitive) Filter the list of accounts to where the name starts with a
particular string.
- **name.endsWith** (string, optional) [query]: (case-insensitive) Filter the list of accounts to where the name ends with a particular
string.
- **name.contains** (string, optional) [query]: (case-insensitive) Filter the list of accounts to where the name contains a particular
string.
- **order_by** (string, optional) [query]: Field to order results by. Currently supported values: `account_name`.
When not specified, results are ordered by internal account ID.
- **direction** (string, optional) [query]: Sort direction for the order_by field. Valid values: `asc`, `desc`.
Defaults to `asc` when order_by is specified.
- **page_token** (string, optional) [query]: An opaque token returned from the last list response that when
provided will retrieve the next page.

Parameters used to filter the retrieved list must remain in subsequent
requests with a page token.
- **page_size** (integer, optional) [query]: The amount of items to return. Defaults to 10.

## Response

### 200

The request has succeeded.

- **errors** (array): 
- **messages** (array): 
- **result** (array): 
- **result_info** (object): 
- **success** (boolean): 

### 4XX

An unexpected error response.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean):
