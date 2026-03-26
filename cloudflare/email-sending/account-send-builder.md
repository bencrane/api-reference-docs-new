# Send an email using the builder.

`POST /accounts/{account_id}/email/sending/send`



## Parameters

- **account_id** (string, required) [path]: Identifier of the account.

## Request Body

- **attachments** (array, optional): File attachments and inline images.
- **bcc** (object, optional): BCC recipient(s). A single email string or an array of email strings.
- **cc** (object, optional): CC recipient(s). A single email string or an array of email strings.
- **from** (object, required): Sender email address. Either a plain string or an object with address and name.
- **headers** (object, optional): Custom email headers as key-value pairs.
- **html** (string, optional): HTML body of the email. At least one of text or html must be provided.
- **reply_to** (object, optional): Reply-to address. Either a plain string or an object with address and name.
- **subject** (string, required): Email subject line.
- **text** (string, optional): Plain text body of the email. At least one of text or html must be provided.
- **to** (object, required): Recipient(s). A single email string or an array of email strings.

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
