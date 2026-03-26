# List organization members

`GET /organizations/{organization_id}/members`

List memberships for an Organization. (Currently in Closed Beta - see https://developers.cloudflare.com/fundamentals/organizations/)

## Parameters

- **organization_id** (string, required) [path]: 
- **status** (array, optional) [query]: Filter the list of memberships by membership status.
- **user.email** (string, optional) [query]: Filter the list of memberships for a specific email.
- **user.email.contains** (string, optional) [query]: Filter the list of memberships for a specific email that contains a substring.
- **user.email.startsWith** (string, optional) [query]: Filter the list of memberships for a specific email that starts with a substring.
- **user.email.endsWith** (string, optional) [query]: Filter the list of memberships for a specific email that ends with a substring.
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
