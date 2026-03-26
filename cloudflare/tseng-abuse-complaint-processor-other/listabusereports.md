# List abuse reports

`GET /accounts/{account_id}/abuse-reports`

List the abuse reports for a given account

## Parameters

- **account_id** (string, required) [path]: Cloudflare Account ID
- **page** (integer, optional) [query]: Where in pagination to start listing abuse reports
- **per_page** (integer, optional) [query]: How many abuse reports per page to list
- **sort** (string, optional) [query]: A property to sort by, followed by the order (id, cdate, domain, type, status)
- **domain** (string, optional) [query]: Filter by domain name related to the abuse report
- **created_before** (string, optional) [query]: Returns reports created before the specified date
- **created_after** (string, optional) [query]: Returns reports created after the specified date
- **status** (string, optional) [query]: Filter by the status of the report.
- **type** (string, optional) [query]: Filter by the type of the report.
- **mitigation_status** (string, optional) [query]: Filter reports that have any mitigations in the given status.

## Response

### 200

Abuse report list successful

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **result_info** (object): 
- **success** (boolean): 

### 500

Failed to retrieve abuse reports

- **errors** (array): 
- **messages** (array): 
- **success** (boolean):
