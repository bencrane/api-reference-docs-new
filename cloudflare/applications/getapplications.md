# Get  applications

`GET /accounts/{accountId}/resource-library/applications`

Get applications with different filters.

## Parameters

- **accountId** (string, required) [path]: Account ID.
- **filter** (string, optional) [query]: Filter applications using key:value format. Supported filter keys:
- name: Filter by application name (e.g., name:HR)
- id: Filter by application ID (e.g., id:0b63249c-95bf-4cc0-a7cc-d7faaaf1dac0)
- human_id: Filter by human-readable ID (e.g., human_id:HR)
- hostname: Filter by hostname or support domain (e.g., hostname:portal.example.com)
- source: Filter by application source name (e.g., source:cloudflare)
- ip_subnet: Filter by IP subnet in CIDR notation (e.g., ip_subnet:192.168.1.0/24).
.

- **limit** (integer, optional) [query]: Limit of number of results to return.
- **offset** (integer, optional) [query]: Offset of results to return.
- **order_by** (string, optional) [query]: Order by result by field name and order (e.g., name:asc).

## Response

### 200

Get the application response.

- **result** (array, optional): Returns the list of applications.

### 4XX

Get application response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Indicates whether the API call was successful. Values: `false`
