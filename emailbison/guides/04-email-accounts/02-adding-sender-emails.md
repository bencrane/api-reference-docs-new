# Adding Email Accounts (Adding Sender Emails)

**URL:** https://docs.emailbison.com/email-accounts/adding-accounts

**Bulk Uploading:** There are multiple ways to bulk upload accounts to EmailBison.

**Custom SMTP Providers (Emails not with Microsoft or Google) - API:**
Send a POST request to the following endpoint: `/api/sender-emails/imap-smtp`. The Content-Type header key should be set to multipart/form-data. The only parameter you must provide is csv, and the value should be your CSV file.

Example:
```
curl https://dedi.emailbison.com/api/sender-emails/bulk \
  --request POST \
  --header 'Content-Type: multipart/form-data' \
  --header 'Authorization: Bearer YOUR_SECRET_TOKEN' \
  --data "{"csv":""}"
```

**Custom SMTP Providers (UI):** Navigate to Email Accounts -> Connect Email Account -> Bulk Upload Custom Provider. Download and refer to the sample CSV file for proper CSV formatting.

**Microsoft Accounts:** The EmailBison team has built and released a native program to bulk upload Microsoft accounts. The download and all instructions can be found on the Bulk Uploader Tool page.

**Google Accounts:** Bulk uploading Google accounts is currently not first-party supported due to the frequent captcha requirements by Google.
