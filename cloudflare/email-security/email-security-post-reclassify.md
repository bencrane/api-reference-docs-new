# Change email classification

`POST /accounts/{account_id}/email-security/investigate/{postfix_id}/reclassify`

Submits an email message for reclassification, updating its threat assessment
based on new analysis.

## Parameters

- **account_id** (string, required) [path]: 
- **postfix_id** (string, required) [path]: 

## Request Body

- **eml_content** (string, optional): Base64 encoded content of the EML file
- **escalated_submission_id** (string, optional): 
- **expected_disposition** (string, required):  Values: `NONE`, `BULK`, `MALICIOUS`, `SPAM`, `SPOOF`, `SUSPICIOUS`

## Response

### 202



- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): 
- **result** (object, optional): 

### 4XX

Client Error

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean):
