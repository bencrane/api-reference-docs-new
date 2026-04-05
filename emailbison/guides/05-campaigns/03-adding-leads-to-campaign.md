# Adding Leads to a Campaign

**URL:** https://docs.emailbison.com/campaigns/adding-leads-to-a-campaign

Adding leads to an active campaign will take up to 5 minutes for the leads to get synced. This ensures that there is no interruption to the campaign's sending.

**Adding leads from existing list (API):**
Send a POST request to the following endpoint: `/api/campaigns/{campaign_id}/leads/attach-lead-list`

The request takes 1 required body parameter:
- **lead_list_id** (integer, required) - The ID of the lead list to add

Example:
```
curl 'https://dedi.emailbison.com/api/campaigns/6/leads/attach-lead-list' \
  --request POST \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer YOUR_SECRET_TOKEN' \
  --data '{
    "lead_list_id": 1
  }'
```

**Adding leads by their IDs (API):**
You can also add individual leads to a campaign using the lead IDs. Send a POST request to: `/api/campaigns/{campaign_id}/leads/attach-leads`

The request takes 1 required body parameter:
- **lead_ids** (array, required) - An array containing the IDs of the leads to add

Example:
```
curl 'https://dedi.emailbison.com/api/campaigns/6/leads/attach-leads' \
  --request POST \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer YOUR_SECRET_TOKEN' \
  --data '{
    "lead_ids": [1,2,3]
  }'
```

**Adding leads (UI):** Navigate to Campaigns. Click on the campaign you want to add leads to. Click the Actions dropdown and click Add more contacts.
