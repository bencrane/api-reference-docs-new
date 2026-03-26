# Submit an abuse report

`POST /accounts/{account_id}/abuse-reports/{report_param}`

Submit the Abuse Report of a particular type

## Parameters

- **account_id** (string, required) [path]: Cloudflare Account ID
- **report_param** (string, required) [path]: The report type to be submitted. Example: abuse_general

## Request Body

One of: object, object, object, object, object, object, object, object

## Response

### 200

Report submitted successfully

- **abuse_rand** (string): The identifier for the submitted abuse report.
- **request** (object): 
- **result** (string): The result should be 'success' for successful response

### 400

Report submitted with an error

- **error_code** (string): 
- **msg** (string): The error message for the error
- **request** (object): 
- **result** (string): The result should be 'error' for successful response

### 500

Report submitted with an error

- **error_code** (string): 
- **msg** (string): The error message for the error
- **request** (object): 
- **result** (string): The result should be 'error' for successful response
