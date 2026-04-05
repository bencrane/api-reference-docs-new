# Fetching Replies (Getting Replies and Campaign Emails For a Lead)

**URL:** https://docs.emailbison.com/master-inbox/fetching-replies

**Getting Replies for a Lead (API):**
Send a GET request to `/api/leads/{lead_id}/replies`

The following are the parameters for the request:
- **lead_id** (integer, required) - The ID or email of the lead.
- **filters** (query parameters):
  - **search** (string|null) - Search term for filtering replies.
  - **status** (string|null) - Filter by status. One of interested, automated_reply, not_automated_reply.
  - **folder** (string|null) - Filter by folder. One of inbox, sent, spam, bounced, all.
  - **read** (boolean|null) - Filter by read status.
  - **campaign_id** (integer|null) - The ID of the campaign.
  - **sender_email_id** (integer|null) - The ID of the sender email address.
  - **tag_ids** (array|null) - Array of tag IDs to filter by.

**Getting Campaign Emails for a Lead (API):**
Send a GET request to `/api/leads/{lead_id_or_email}/sent-emails`

The following are the parameters for the request:
- **lead_id_or_email** (integer, required) - The ID or email of the lead.
