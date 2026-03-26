# List Cloudflare colos

`GET /accounts/{account_id}/dex/colos`

List Cloudflare colos that account's devices were connected to during a time period, sorted by usage starting from the most used colo. Colos without traffic are also returned and sorted alphabetically.

## Parameters

- **account_id** (string, required) [path]: unique identifier linked to an account in the API request path.
- **from** (string, required) [query]: Start time for connection period in ISO (RFC3339 - ISO 8601) format
- **to** (string, required) [query]: End time for connection period in ISO (RFC3339 - ISO 8601) format
- **sortBy** (string, optional) [query]: Type of usage that colos should be sorted by. If unspecified, returns all Cloudflare colos sorted alphabetically.

## Response

### 200

List colos response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (array, optional): array of colos.

### 4XX

List colos failure response

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
