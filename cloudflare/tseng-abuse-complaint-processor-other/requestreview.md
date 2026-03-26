# Request review on mitigations

`POST /accounts/{account_id}/abuse-reports/{report_id}/mitigations/appeal`

Request a review for mitigations on an account.

## Parameters

- **account_id** (string, required) [path]: Cloudflare Account ID
- **report_id** (string, required) [path]: Abuse Report ID

## Request Body

- **appeals** (array, required): List of mitigations to appeal.

## Response

### 200

Mitigation appeals received

- **errors** (array): 
- **messages** (array): 
- **result** (array): 
- **result_info** (object): 
- **success** (boolean): 

### 500

Failed to request review on delayed action.

- **errors** (array): 
- **messages** (array): 
- **success** (boolean):
