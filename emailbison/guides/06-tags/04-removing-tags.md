# Removing Tags

**URL:** https://docs.emailbison.com/tags/removing-tags

**API:**
Send a DELETE request to one of the following endpoints:
- `/api/tags/attach-to-sender-emails`
- `/api/tags/attach-to-leads`
- `/api/tags/attach-to-campaigns`

The fields for these endpoints are:
- **tag_ids** (array, required) - An array of tag IDs to remove.
- **{taggable}_ids** (array, required) - An array of taggables to remove the tags from. One of sender_email_ids, lead_ids, campaign_ids.

Example:
```
curl https://dedi.emailbison.com/api/tags/attach-to-sender-emails \
  --request DELETE \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer YOUR_SECRET_TOKEN' \
  --data '{
    "tag_ids": [1, 2],
    "sender_email_ids": [3, 4]
  }'
```

**UI:** Navigate to the Campaigns, Email Accounts, or Contacts tab. Filter and select taggables by clicking on the checkboxes on the left hand side. After selecting, a Remove tags button will appear. Select tags from the dropdown, and click Remove tags.
