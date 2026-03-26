# Delete organization member

`DELETE /organizations/{organization_id}/members/{member_id}`

Delete a membership to a particular Organization. (Currently in Closed Beta - see https://developers.cloudflare.com/fundamentals/organizations/)

## Parameters

- **organization_id** (string, required) [path]: 
- **member_id** (string, required) [path]: 

## Request Body

- **member_id** (string, required): Organization Member ID

## Response

### 204

There is no content to send for this request, but the headers may be useful.

### 4XX

An unexpected error response.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean):
