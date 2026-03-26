# List abuse report emails

`GET /accounts/{account_id}/abuse-reports/{report_id}/emails`

List emails sent to the customer for an abuse report. Returns all successful customer emails sent for the specified abuse report. Does not include emails sent to hosts or submitters.

## Parameters

- **account_id** (string, required) [path]: Cloudflare Account ID
- **report_id** (string, required) [path]: Abuse Report ID
- **page** (integer, optional) [query]: Page number to retrieve (default 1)
- **per_page** (integer, optional) [query]: Number of emails per page (default 20, max 100)

## Response

### 200

List abuse report emails successful

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **result_info** (object): 
- **success** (boolean): 

### 400

Bad request - invalid parameters or report not found

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): 

### 500

Failed to list abuse report emails

- **errors** (array): 
- **messages** (array): 
- **success** (boolean):
