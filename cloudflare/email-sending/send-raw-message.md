# Send a raw MIME email message.

`POST /accounts/{account_id}/email/sending/send_raw`



## Parameters

- **account_id** (string, required) [path]: Identifier of the account.

## Request Body

- **from** (string, required): Sender email address.
- **mime_message** (string, required): The full MIME-encoded email message. Should include standard RFC 5322 headers such as From, To, Subject, and Content-Type. The from and recipients fields in the request body control SMTP envelope routing; the From and To headers in the MIME message control what the recipient's email client displays.
- **recipients** (array, required): List of recipient email addresses.

## Response

### 200

Email sending results.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **result_info** (object): 
- **success** (boolean): 

### 400

Invalid request, generally because of the format/content of the email send request. No email will be sent when this happens.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): 

### 403

Email sending is disabled for this zone/account.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): 

### 429

Account/zone has surpassed the rate at which it can send email, please try again later. No email will be sent when this happens.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): 

### 500

An unexpected error while processing the email send request. No email will be sent when this happens.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean):
