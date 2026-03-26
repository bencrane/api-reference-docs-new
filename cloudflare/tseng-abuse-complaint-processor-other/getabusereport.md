# Abuse Report Details

`GET /accounts/{account_id}/abuse-reports/{report_param}`

Retrieve the details of an abuse report.

## Parameters

- **account_id** (string, required) [path]: Cloudflare Account ID
- **report_param** (string, required) [path]: Identifier of the abuse report

## Response

### 200

Report submitted successfully

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): 

### 400

Report submitted with an error

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): 

### 500

Report submitted with an error

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean):
