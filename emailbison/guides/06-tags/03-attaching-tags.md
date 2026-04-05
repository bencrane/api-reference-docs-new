# Attaching Tags

**URL:** https://docs.emailbison.com/tags/attaching-tags

Tags can be attached to any taggable -- leads, sender emails, and campaigns.

**API:**
Send a POST request to one of the following endpoints:
- `/api/tags/attach-to-sender-emails`
- `/api/tags/attach-to-leads`
- `/api/tags/attach-to-campaigns`

The fields for these endpoints are:
- **tag_ids** (array, required) - An array of tag IDs to attach
- **{taggable}_ids** (array, required) - An array of taggables to attach the tags to. One of sender_email_ids, lead_ids, campaign_ids.

Example:
```
curl https://dedi.emailbison.com/api/tags/attach-to-sender-emails \
  --request POST \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer YOUR_SECRET_TOKEN' \
  --data '{
    "tag_ids": [1, 2],
    "sender_email_ids": [3, 4]
  }'
```

**UI:** Navigate to the Campaigns, Email Accounts, or Contacts tab. Filter and select taggables by clicking on the checkboxes on the left hand side. After selecting, an Add tags button will appear. Select tags from the dropdown, and click Attach tags.
