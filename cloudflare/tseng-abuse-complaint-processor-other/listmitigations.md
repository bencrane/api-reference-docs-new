# List abuse report mitigations

`GET /accounts/{account_id}/abuse-reports/{report_id}/mitigations`

List mitigations done to remediate the abuse report.

## Parameters

- **account_id** (string, required) [path]: Cloudflare Account ID
- **report_id** (string, required) [path]: Abuse Report ID
- **page** (integer, optional) [query]: Where in pagination to start listing abuse reports
- **per_page** (integer, optional) [query]: How many abuse reports per page to list
- **sort** (string, optional) [query]: A property to sort by, followed by the order
- **type** (string, optional) [query]: Filter by the type of mitigation. This filter parameter can be specified multiple times to include multiple types of mitigations in the result set, e.g. ?type=rate_limit_cache&type=legal_block.
- **effective_before** (string, optional) [query]: Returns mitigations that were dispatched before the given date
- **effective_after** (string, optional) [query]: Returns mitigation that were dispatched after the given date
- **status** (string, optional) [query]: Filter by the status of the mitigation.
- **entity_type** (string, optional) [query]: Filter by the type of entity the mitigation impacts.

## Response

### 200

List abuse report mitigations successful

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **result_info** (object): 
- **success** (boolean): 

### 500

Failed to list abuse report mitigations

- **errors** (array): 
- **messages** (array): 
- **success** (boolean):
