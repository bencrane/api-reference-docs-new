# Adding and Removing Sender Emails

**URL:** https://docs.emailbison.com/campaigns/adding-and-removing-sender-emails

**Adding Sender Emails:**
Send a POST request to the following endpoint: `/api/campaigns/{campaign_id}/attach-sender-emails`

The request takes 1 required body parameter:
- **sender_email_ids** (array, required) - An array containing the IDs of the sender emails to add

Example:
```
curl 'https://dedi.emailbison.com/api/campaigns/6/attach-sender-emails' \
  --request POST \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer YOUR_SECRET_TOKEN' \
  --data '{
    "sender_email_ids": [1,2,3]
  }'
```

**Removing Sender Emails:**
Send a DELETE request to the following endpoint: `/api/campaigns/{campaign_id}/remove-sender-emails`

The request takes 1 required body parameter:
- **sender_email_ids** (array, required) - An array containing the IDs of the sender emails to remove

Example:
```
curl 'https://dedi.emailbison.com/api/campaigns/6/remove-sender-emails' \
  --request POST \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer YOUR_SECRET_TOKEN' \
  --data '{
    "sender_email_ids": [1,2,3]
  }'
```
