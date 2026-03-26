# List organizations the user has access to

`GET /organizations`

Retrieve a list of organizations a particular user has access to. (Currently in Closed Beta - see https://developers.cloudflare.com/fundamentals/organizations/)

## Parameters

- **id** (array, optional) [query]: Only return organizations with the specified IDs (ex. id=foo&id=bar). Send multiple elements
by repeating the query value.
- **name** (string, optional) [query]: (case-sensitive) Filter the list of organizations to where the name is equal to a
particular string.
- **name.startsWith** (string, optional) [query]: (case-insensitive) Filter the list of organizations to where the name starts with a
particular string.
- **name.endsWith** (string, optional) [query]: (case-insensitive) Filter the list of organizations to where the name ends with a particular
string.
- **name.contains** (string, optional) [query]: (case-insensitive) Filter the list of organizations to where the name contains a particular
string.
- **containing.account** (string, optional) [query]: Filter the list of organizations to the ones that contain this particular
account.
- **containing.user** (string, optional) [query]: Filter the list of organizations to the ones that contain this particular
user.

IMPORTANT: Just because an organization "contains" a user is not a
representation of any authorization or privilege to manage any resources
therein. An organization "containing" a user simply means the user is managed by
that organization.
- **containing.organization** (string, optional) [query]: Filter the list of organizations to the ones that contain this particular
organization.
- **parent.id** (string, optional) [query]: Filter the list of organizations to the ones that are a sub-organization
of the specified organization.

"null" is a valid value to provide for this parameter. It means "where
an organization has no parent (i.e. it is a 'root' organization)."
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
