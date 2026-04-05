# Responding to Messages

**URL:** https://docs.emailbison.com/master-inbox/responding-to-messages

Send a POST request to the following endpoint: `/api/replies/{reply_id}/reply`

The following are the parameters for the request:
- **reply_id** (integer, required) - The ID of the parent reply.
- **message** (string, required) - The contents of the reply
- **sender_email_id** (integer, required) - The ID of the sender email
- **to_emails** (array, required) - Array of people to send this email to. The name field in the object can be nulled (left empty). Example: `[{"name": "John Doe", "email_address": "john@example.com"}]`
- **inject_previous_email_body** (boolean|null) - Whether to inject the body of the previous email into this email. If nothing sent, false is assumed
- **content_type** (string) - Type of the email (html or text)
- **cc_emails** (array) - An array of people to send a copy of this email to (Carbon Copy). Example: `[{"name": "John Doe", "email_address": "john@example.com"}]`
- **bcc_emails** (array) - An array of people to send a blind copy of this email to (Blind Carbon Copy). Example: `[{"name": "John Doe", "email_address": "john@example.com"}]`
